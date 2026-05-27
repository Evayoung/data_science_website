-- Segun Banji portfolio schema and seed data for Supabase/Postgres.
-- Run this in the Supabase SQL editor.
-- Re-running this script resets portfolio content tables, but does not clear contact_messages.

begin;

create extension if not exists pgcrypto;

-- ---------------------------------------------------------------------------
-- Core profile/content tables
-- ---------------------------------------------------------------------------
create table if not exists public.portfolio_profiles (
  id text primary key,
  name text not null,
  initials text not null,
  title text not null,
  tagline text not null,
  phone text,
  email text not null,
  linkedin_url text,
  github_url text,
  location text,
  summary text,
  how_i_work text,
  youtube_channel_url text,
  availability text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.portfolio_bio_paragraphs (
  id bigserial primary key,
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  body text not null,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_stats (
  id bigserial primary key,
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  value integer not null,
  suffix text not null default '',
  label text not null,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_skills (
  id bigserial primary key,
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  name text not null,
  group_name text,
  proficiency smallint check (proficiency between 0 and 100),
  show_on_home boolean not null default false,
  show_on_cv boolean not null default false,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_social_links (
  id bigserial primary key,
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  label text not null,
  icon text not null,
  href text not null,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_specialisations (
  id bigserial primary key,
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  icon text not null,
  title text not null,
  description text not null,
  sort_order integer not null default 0
);

-- ---------------------------------------------------------------------------
-- CV tables
-- ---------------------------------------------------------------------------
create table if not exists public.portfolio_experience (
  id uuid primary key default gen_random_uuid(),
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  role text not null,
  organization text not null,
  location text,
  date_label text not null,
  description text not null,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_experience_highlights (
  id bigserial primary key,
  experience_id uuid not null references public.portfolio_experience(id) on delete cascade,
  body text not null,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_education (
  id bigserial primary key,
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  degree text not null,
  institution text not null,
  location text,
  year text not null,
  gpa text,
  honors text,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_certifications (
  id bigserial primary key,
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  title text not null,
  issuer text,
  date_label text,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_languages (
  id bigserial primary key,
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  label text not null,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_soft_skills (
  id bigserial primary key,
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  label text not null,
  sort_order integer not null default 0
);

-- ---------------------------------------------------------------------------
-- Projects and videos
-- ---------------------------------------------------------------------------
create table if not exists public.work_categories (
  id text primary key,
  label text not null,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_projects (
  slug text primary key,
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  title text not null,
  category_id text not null references public.work_categories(id),
  project_year text,
  description text not null,
  detail text not null,
  image_path text,
  featured boolean not null default false,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_project_tools (
  id bigserial primary key,
  project_slug text not null references public.portfolio_projects(slug) on delete cascade,
  name text not null,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_project_links (
  id bigserial primary key,
  project_slug text not null references public.portfolio_projects(slug) on delete cascade,
  label text not null,
  url text not null,
  sort_order integer not null default 0
);

create table if not exists public.video_categories (
  id text primary key,
  label text not null,
  sort_order integer not null default 0
);

create table if not exists public.portfolio_videos (
  id bigserial primary key,
  profile_id text not null references public.portfolio_profiles(id) on delete cascade,
  video_id text not null,
  title text not null,
  description text not null,
  category_id text not null references public.video_categories(id),
  sort_order integer not null default 0
);

-- ---------------------------------------------------------------------------
-- Optional form capture table. Keep SMTP in the app if preferred.
-- ---------------------------------------------------------------------------
create table if not exists public.contact_messages (
  id uuid primary key default gen_random_uuid(),
  name text not null check (char_length(name) between 2 and 120),
  email text not null check (email ~* '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$'),
  subject text not null check (char_length(subject) between 2 and 160),
  message text not null check (char_length(message) between 10 and 5000),
  source text not null default 'portfolio',
  created_at timestamptz not null default now()
);

-- ---------------------------------------------------------------------------
-- Indexes for common reads, joins, and filters.
-- ---------------------------------------------------------------------------
create index if not exists portfolio_bio_profile_order_idx on public.portfolio_bio_paragraphs(profile_id, sort_order);
create index if not exists portfolio_stats_profile_order_idx on public.portfolio_stats(profile_id, sort_order);
create index if not exists portfolio_skills_profile_context_idx on public.portfolio_skills(profile_id, show_on_home, show_on_cv, group_name, sort_order);
create index if not exists portfolio_social_profile_order_idx on public.portfolio_social_links(profile_id, sort_order);
create index if not exists portfolio_specialisations_profile_order_idx on public.portfolio_specialisations(profile_id, sort_order);
create index if not exists portfolio_experience_profile_order_idx on public.portfolio_experience(profile_id, sort_order);
create index if not exists portfolio_experience_highlights_parent_order_idx on public.portfolio_experience_highlights(experience_id, sort_order);
create index if not exists portfolio_education_profile_order_idx on public.portfolio_education(profile_id, sort_order);
create index if not exists portfolio_certifications_profile_order_idx on public.portfolio_certifications(profile_id, sort_order);
create index if not exists portfolio_projects_profile_order_idx on public.portfolio_projects(profile_id, sort_order);
create index if not exists portfolio_projects_category_idx on public.portfolio_projects(category_id, featured, sort_order);
create index if not exists portfolio_project_tools_slug_order_idx on public.portfolio_project_tools(project_slug, sort_order);
create index if not exists portfolio_project_links_slug_order_idx on public.portfolio_project_links(project_slug, sort_order);
create index if not exists portfolio_videos_category_order_idx on public.portfolio_videos(category_id, sort_order);
create index if not exists contact_messages_created_at_idx on public.contact_messages(created_at desc);

-- ---------------------------------------------------------------------------
-- RLS: public portfolio content is readable; contact messages are insert-only.
-- ---------------------------------------------------------------------------
alter table public.portfolio_profiles enable row level security;
alter table public.portfolio_bio_paragraphs enable row level security;
alter table public.portfolio_stats enable row level security;
alter table public.portfolio_skills enable row level security;
alter table public.portfolio_social_links enable row level security;
alter table public.portfolio_specialisations enable row level security;
alter table public.portfolio_experience enable row level security;
alter table public.portfolio_experience_highlights enable row level security;
alter table public.portfolio_education enable row level security;
alter table public.portfolio_certifications enable row level security;
alter table public.portfolio_languages enable row level security;
alter table public.portfolio_soft_skills enable row level security;
alter table public.work_categories enable row level security;
alter table public.portfolio_projects enable row level security;
alter table public.portfolio_project_tools enable row level security;
alter table public.portfolio_project_links enable row level security;
alter table public.video_categories enable row level security;
alter table public.portfolio_videos enable row level security;
alter table public.contact_messages enable row level security;

drop policy if exists portfolio_profiles_public_read on public.portfolio_profiles;
create policy portfolio_profiles_public_read on public.portfolio_profiles for select to anon, authenticated using (true);
drop policy if exists portfolio_bio_public_read on public.portfolio_bio_paragraphs;
create policy portfolio_bio_public_read on public.portfolio_bio_paragraphs for select to anon, authenticated using (true);
drop policy if exists portfolio_stats_public_read on public.portfolio_stats;
create policy portfolio_stats_public_read on public.portfolio_stats for select to anon, authenticated using (true);
drop policy if exists portfolio_skills_public_read on public.portfolio_skills;
create policy portfolio_skills_public_read on public.portfolio_skills for select to anon, authenticated using (true);
drop policy if exists portfolio_social_public_read on public.portfolio_social_links;
create policy portfolio_social_public_read on public.portfolio_social_links for select to anon, authenticated using (true);
drop policy if exists portfolio_specialisations_public_read on public.portfolio_specialisations;
create policy portfolio_specialisations_public_read on public.portfolio_specialisations for select to anon, authenticated using (true);
drop policy if exists portfolio_experience_public_read on public.portfolio_experience;
create policy portfolio_experience_public_read on public.portfolio_experience for select to anon, authenticated using (true);
drop policy if exists portfolio_experience_highlights_public_read on public.portfolio_experience_highlights;
create policy portfolio_experience_highlights_public_read on public.portfolio_experience_highlights for select to anon, authenticated using (true);
drop policy if exists portfolio_education_public_read on public.portfolio_education;
create policy portfolio_education_public_read on public.portfolio_education for select to anon, authenticated using (true);
drop policy if exists portfolio_certifications_public_read on public.portfolio_certifications;
create policy portfolio_certifications_public_read on public.portfolio_certifications for select to anon, authenticated using (true);
drop policy if exists portfolio_languages_public_read on public.portfolio_languages;
create policy portfolio_languages_public_read on public.portfolio_languages for select to anon, authenticated using (true);
drop policy if exists portfolio_soft_skills_public_read on public.portfolio_soft_skills;
create policy portfolio_soft_skills_public_read on public.portfolio_soft_skills for select to anon, authenticated using (true);
drop policy if exists work_categories_public_read on public.work_categories;
create policy work_categories_public_read on public.work_categories for select to anon, authenticated using (true);
drop policy if exists portfolio_projects_public_read on public.portfolio_projects;
create policy portfolio_projects_public_read on public.portfolio_projects for select to anon, authenticated using (true);
drop policy if exists portfolio_project_tools_public_read on public.portfolio_project_tools;
create policy portfolio_project_tools_public_read on public.portfolio_project_tools for select to anon, authenticated using (true);
drop policy if exists portfolio_project_links_public_read on public.portfolio_project_links;
create policy portfolio_project_links_public_read on public.portfolio_project_links for select to anon, authenticated using (true);
drop policy if exists video_categories_public_read on public.video_categories;
create policy video_categories_public_read on public.video_categories for select to anon, authenticated using (true);
drop policy if exists portfolio_videos_public_read on public.portfolio_videos;
create policy portfolio_videos_public_read on public.portfolio_videos for select to anon, authenticated using (true);
drop policy if exists contact_messages_public_insert on public.contact_messages;
create policy contact_messages_public_insert on public.contact_messages
  for insert to anon, authenticated
  with check (
    char_length(name) between 2 and 120
    and char_length(subject) between 2 and 160
    and char_length(message) between 10 and 5000
  );

grant usage on schema public to anon, authenticated;
grant select on
  public.portfolio_profiles,
  public.portfolio_bio_paragraphs,
  public.portfolio_stats,
  public.portfolio_skills,
  public.portfolio_social_links,
  public.portfolio_specialisations,
  public.portfolio_experience,
  public.portfolio_experience_highlights,
  public.portfolio_education,
  public.portfolio_certifications,
  public.portfolio_languages,
  public.portfolio_soft_skills,
  public.work_categories,
  public.portfolio_projects,
  public.portfolio_project_tools,
  public.portfolio_project_links,
  public.video_categories,
  public.portfolio_videos
to anon, authenticated;
grant insert on public.contact_messages to anon, authenticated;

-- ---------------------------------------------------------------------------
-- Seed data
-- ---------------------------------------------------------------------------
truncate table
  public.portfolio_bio_paragraphs,
  public.portfolio_stats,
  public.portfolio_skills,
  public.portfolio_social_links,
  public.portfolio_specialisations,
  public.portfolio_experience_highlights,
  public.portfolio_experience,
  public.portfolio_education,
  public.portfolio_certifications,
  public.portfolio_languages,
  public.portfolio_soft_skills,
  public.portfolio_project_links,
  public.portfolio_project_tools,
  public.portfolio_projects,
  public.work_categories,
  public.portfolio_videos,
  public.video_categories,
  public.portfolio_profiles
restart identity cascade;

insert into public.portfolio_profiles (
  id, name, initials, title, tagline, phone, email, linkedin_url, github_url,
  location, summary, how_i_work, youtube_channel_url, availability
) values (
  'segun-banji',
  'Segun Banji',
  'SB',
  'Data Analyst & Digital Consultant',
  '7+ years using Excel, SQL, and Power BI to improve operations, reporting, and business intelligence decisions.',
  '+2348138720817',
  'banjisegun99@gmail.com',
  'https://linkedin.com/in/banjisegun',
  'https://github.com/banjisegun99',
  'Satellite Town, Lagos',
  'Data Analyst and Digital Consultant with 7+ years of experience using Excel, SQL, and Power BI to drive operational efficiency in logistics and business intelligence. Proven record of improving reporting accuracy by 35%, reducing operational costs by 20%, and automating analytics processes for decision-making. Passionate about leveraging data insights to optimize business performance and digital strategy.',
  'I start with the operational decision behind the data, then design the cleanest path from collection to insight: Excel for practical modelling, SQL for validation and transformation, and Power BI for dashboards stakeholders can act on quickly.',
  '#',
  'Available for consulting'
);

insert into public.portfolio_bio_paragraphs (profile_id, body, sort_order) values
('segun-banji', 'I am a Data Analyst and Digital Consultant with 7+ years of experience using Excel, SQL, and Power BI to turn operational data into decisions that improve accuracy, cost control, and business performance.', 1),
('segun-banji', 'My recent work spans logistics data frameworks, Excel analytical models, Power BI dashboards, SQL data validation, and training programs that make analytics practical for business teams and young learners.', 2);

insert into public.portfolio_stats (profile_id, value, suffix, label, sort_order) values
('segun-banji', 50, 'k+', 'Records Cleaned Monthly', 1),
('segun-banji', 7, '+', 'Years Experience', 2),
('segun-banji', 200, '+', 'People Trained', 3),
('segun-banji', 35, '%', 'Accuracy Improvement', 4);

insert into public.portfolio_skills (profile_id, name, group_name, proficiency, show_on_home, show_on_cv, sort_order) values
('segun-banji', 'SQL', 'Databases', 90, true, true, 1),
('segun-banji', 'Microsoft Excel', 'Analytics & BI', 95, true, true, 2),
('segun-banji', 'Power BI', 'Analytics & BI', 92, true, true, 3),
('segun-banji', 'Data Cleaning', 'Capabilities', 90, true, true, 4),
('segun-banji', 'Business Intelligence', 'Capabilities', 90, true, true, 5),
('segun-banji', 'Dashboard Design', 'Capabilities', null, true, false, 6),
('segun-banji', 'Data Validation', 'Capabilities', null, true, false, 7),
('segun-banji', 'Reporting Automation', 'Capabilities', 88, true, true, 8),
('segun-banji', 'Operational Analytics', 'Capabilities', null, true, false, 9),
('segun-banji', 'Market Analysis', 'Capabilities', null, true, false, 10),
('segun-banji', 'Data Storytelling', 'Capabilities', null, true, false, 11),
('segun-banji', 'Digital Consulting', 'Capabilities', null, true, false, 12),
('segun-banji', 'Python for Data Analysis', 'Programming', null, false, false, 13),
('segun-banji', 'Business Intelligence Reporting', 'Capabilities', null, false, false, 14),
('segun-banji', 'Digital Strategy', 'Capabilities', null, false, false, 15),
('segun-banji', 'Training & Facilitation', 'Capabilities', null, false, false, 16);

insert into public.portfolio_social_links (profile_id, label, icon, href, sort_order) values
('segun-banji', 'LinkedIn', 'linkedin', 'https://linkedin.com/in/banjisegun', 1),
('segun-banji', 'GitHub', 'github', 'https://github.com/banjisegun99', 2),
('segun-banji', 'Email', 'envelope-fill', 'mailto:banjisegun99@gmail.com', 3);

insert into public.portfolio_specialisations (profile_id, icon, title, description, sort_order) values
('segun-banji', 'graph-up-arrow', 'Operational Analytics', 'Logistics and business performance analysis built around accuracy, cost control, KPI visibility, and decision-ready reporting.', 1),
('segun-banji', 'bar-chart-line-fill', 'BI Dashboards & Reporting', 'Excel and Power BI dashboards that help teams monitor performance, spot variance, and act faster.', 2),
('segun-banji', 'mortarboard-fill', 'Analytics Training', 'Practical analytics training across Excel, Power BI, SQL, and data storytelling for business teams and youth programs.', 3);

insert into public.portfolio_experience (id, profile_id, role, organization, location, date_label, description, sort_order) values
('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaa1', 'segun-banji', 'Digital Consultant & Data Analyst', 'McMoren Logistics Company', 'Lagos, Nigeria', 'Nov 2020 - Present', 'Built logistics data frameworks, Excel analytical models, and performance dashboards that improved reporting accuracy, delivery efficiency, compliance, and fuel-cost visibility.', 1),
('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaa2', 'segun-banji', 'Business Analyst', 'McAdur Imagination Cafe', 'Lagos, Nigeria', 'Aug 2016 - Sept 2019', 'Collected, cleaned, transformed, and validated multi-country business datasets to improve reporting accuracy and reveal customer and sales patterns.', 2);

insert into public.portfolio_experience_highlights (experience_id, body, sort_order) values
('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaa1', 'Designed a data collection framework that improved logistics data accuracy by 35% and reduced reporting delays by 25%.', 1),
('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaa1', 'Developed Excel-based analytical models and performance dashboards to monitor fleet movement and KPIs, enhancing delivery efficiency by 20%.', 2),
('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaa1', 'Integrated traffic and regulatory datasets into internal systems, supporting 100% transport and safety compliance.', 3),
('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaa1', 'Filtered, validated, and automated cleaning for 50,000+ operational records monthly.', 4),
('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaa1', 'Conducted trend and variance analyses that led to a 15% reduction in fuel costs and better route planning.', 5),
('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaa2', 'Collected, cleaned, and transformed multi-country datasets, improving reporting accuracy by 30%.', 1),
('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaa2', 'Corrected data inconsistencies across multiple databases, reducing processing errors by 40% through validation and standardization.', 2),
('aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaa2', 'Delivered data-driven reports that influenced strategic decisions and boosted sales performance by 18%.', 3);

insert into public.portfolio_education (profile_id, degree, institution, location, year, gpa, honors, sort_order) values
('segun-banji', 'Bachelor of Science in Statistics', 'University of Ilorin', 'Kwara State, Nigeria', '2019', '3.77/5.00', 'Second Class Upper', 1);

insert into public.portfolio_certifications (profile_id, title, issuer, date_label, sort_order) values
('segun-banji', 'Data Analytics and Business Intelligence', 'Dataleum Academy', 'May 2023 - June 2023', 1),
('segun-banji', 'SQL Database (Beginner & Intermediate)', 'Sololearn Academy', null, 2),
('segun-banji', 'Python for Data Analysis (Beginner)', 'Sololearn Academy', null, 3),
('segun-banji', 'Data Analytics Essentials', 'Cisco Networking Academy', null, 4);

insert into public.portfolio_languages (profile_id, label, sort_order) values
('segun-banji', 'English - Fluent', 1);

insert into public.portfolio_soft_skills (profile_id, label, sort_order) values
('segun-banji', 'Analytical Thinking', 1),
('segun-banji', 'Communication', 2),
('segun-banji', 'Problem Solving', 3),
('segun-banji', 'Team Collaboration', 4),
('segun-banji', 'Attention to Detail', 5);

insert into public.work_categories (id, label, sort_order) values
('all', 'All', 1),
('analysis', 'Data Analysis', 2),
('bi-dashboards', 'BI Dashboards', 3),
('education', 'Education', 4);

insert into public.portfolio_projects (slug, profile_id, title, category_id, project_year, description, detail, image_path, featured, sort_order) values
('customer-laptop-preference-analytics', 'segun-banji', 'Customer Laptop Preference Analytics', 'analysis', '2025', 'PC market survey analytics identifying customer preferences across 10 major laptop brands.', 'Conducted PC market survey analytics to identify customer preferences across 10 major laptop brands. Cleaned, modelled, and visualized survey data in Excel and Power BI, revealing trends in performance, affordability, design priorities, buying behavior, and pricing sensitivity.', '/assets/images/projects/sales-analysis.jpg', true, 1),
('hewwelt-data-job-research', 'segun-banji', 'Hewwelt Data Job Research', 'bi-dashboards', '2024', 'SQL and Power BI recruitment analytics for 50,000+ job data entries.', 'Processed and validated 50,000+ recruitment data entries using SQL, then designed interactive Power BI dashboards for hiring metrics and recruitment trends. The work improved HR reporting efficiency by 25% and produced strategic recommendations for recruitment optimization.', '/assets/images/projects/sql-supply-chain.jpg', true, 2),
('digprom-analytics', 'segun-banji', 'Digprom Analytics', 'analysis', '2023', 'Customer-record cleaning, ETL preparation, and churn insight reporting.', 'Cleaned and transformed over 100,000 customer records with SQL and Power BI, improving model readiness by 35%. Designed automated ETL data pipelines for churn prediction, reducing manual processing time by 40% and supporting data-driven retention strategies.', '/assets/images/projects/mcmoren-dashboard.jpg', true, 3),
('kwara-tech-for-youths-initiative', 'segun-banji', 'Kwara Tech for Youths'' Initiative', 'education', '2022', 'Youth empowerment analytics and Excel/Power BI training for 200+ participants.', 'Collaborated with a state technology office to deliver data-driven youth empowerment programs, training 200+ participants in Excel and Power BI. Led analysis on training performance metrics and created dashboards for government reporting and stakeholder presentations.', '/assets/images/projects/midramo-curriculum.jpg', false, 4),
('kid-tech-coding-program', 'segun-banji', 'Kid Tech Coding Program', 'education', '2021', 'Analytics modules introducing children aged 8-15 to data storytelling and visualization.', 'Developed analytics modules for children aged 8-15, simplifying concepts like data storytelling and Power BI dashboards. Evaluated participant performance data to improve teaching content and increase learner engagement by 45%.', '/assets/images/projects/excel-vba.jpg', false, 5);

insert into public.portfolio_project_tools (project_slug, name, sort_order) values
('customer-laptop-preference-analytics', 'Excel', 1),
('customer-laptop-preference-analytics', 'Power BI', 2),
('hewwelt-data-job-research', 'SQL', 1),
('hewwelt-data-job-research', 'Power BI', 2),
('digprom-analytics', 'SQL', 1),
('digprom-analytics', 'Power BI', 2),
('kwara-tech-for-youths-initiative', 'Excel', 1),
('kwara-tech-for-youths-initiative', 'Power BI', 2),
('kid-tech-coding-program', 'Excel', 1),
('kid-tech-coding-program', 'Power BI', 2);

insert into public.video_categories (id, label, sort_order) values
('all', 'All', 1),
('tutorials', 'Tutorials', 2),
('walkthroughs', 'Walkthroughs', 3),
('case-studies', 'Case Studies', 4);

insert into public.portfolio_videos (profile_id, video_id, title, description, category_id, sort_order) values
('segun-banji', 'dQw4w9WgXcQ', 'Getting Started with Power BI - A Practical Guide', 'Build your first interactive dashboard in Power BI from scratch using real business data.', 'tutorials', 1),
('segun-banji', 'dQw4w9WgXcQ', 'SQL for Data Analysts - Core Queries You Must Know', 'Master SELECT, JOIN, GROUP BY, and window functions with real-world examples.', 'tutorials', 2),
('segun-banji', 'dQw4w9WgXcQ', 'Cleaning Messy Data with Python Pandas', 'Step-by-step walkthrough of handling nulls, duplicates, type errors, and outliers.', 'walkthroughs', 3),
('segun-banji', 'dQw4w9WgXcQ', 'How I Built a Logistics Dashboard', 'A behind-the-scenes case study on Power BI dashboard design for logistics.', 'case-studies', 4);

commit;
