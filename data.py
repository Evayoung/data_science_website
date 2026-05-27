"""
Shared content data for Segun Banji's Data Science Portfolio.
"""

# ---------------------------------------------------------------------------
# OWNER
# ---------------------------------------------------------------------------
OWNER = {
    "name": "Segun Banji",
    "initials": "SB",
    "title": "Data Analyst & Digital Consultant",
    "tagline": (
        "7+ years using Excel, SQL, and Power BI to improve operations, "
        "reporting, and business intelligence decisions."
    ),
    "phone": "+2348138720817",
    "email": "banjisegun99@gmail.com",
    "linkedin": "https://linkedin.com/in/banjisegun",
    "github": "https://github.com/banjisegun99",
    "location": "Satellite Town, Lagos",
    "summary": (
        "Data Analyst and Digital Consultant with 7+ years of experience using "
        "Excel, SQL, and Power BI to drive operational efficiency in logistics "
        "and business intelligence. Proven record of improving reporting accuracy "
        "by 35%, reducing operational costs by 20%, and automating analytics "
        "processes for decision-making. Passionate about leveraging data insights "
        "to optimize business performance and digital strategy."
    ),
    "bio": [
        (
            "I am a Data Analyst and Digital Consultant with 7+ years of experience "
            "using Excel, SQL, and Power BI to turn operational data into decisions "
            "that improve accuracy, cost control, and business performance."
        ),
        (
            "My recent work spans logistics data frameworks, Excel analytical models, "
            "Power BI dashboards, SQL data validation, and training programs that "
            "make analytics practical for business teams and young learners."
        ),
    ],
    "how_i_work": (
        "I start with the operational decision behind the data, then design the "
        "cleanest path from collection to insight: Excel for practical modelling, "
        "SQL for validation and transformation, and Power BI for dashboards "
        "stakeholders can act on quickly."
    ),
    "youtube_channel": "#",
    "availability": "Available for consulting",
}

# ---------------------------------------------------------------------------
# STATS (home page)
# ---------------------------------------------------------------------------
STATS = [
    {"value": 50, "suffix": "k+", "label": "Records Cleaned Monthly"},
    {"value": 7, "suffix": "+", "label": "Years Experience"},
    {"value": 200, "suffix": "+", "label": "People Trained"},
    {"value": 35, "suffix": "%", "label": "Accuracy Improvement"},
]

# ---------------------------------------------------------------------------
# SKILLS (flat list for home skills strip)
# ---------------------------------------------------------------------------
SKILLS_FLAT = [
    "SQL",
    "Microsoft Excel",
    "Power BI",
    "Data Cleaning",
    "Business Intelligence",
    "Dashboard Design",
    "Data Validation",
    "Reporting Automation",
    "Operational Analytics",
    "Market Analysis",
    "Data Storytelling",
    "Digital Consulting",
]

# ---------------------------------------------------------------------------
# TOOLS (grouped for About page)
# ---------------------------------------------------------------------------
TOOLS = {
    "Analytics & BI": ["Microsoft Excel", "Power BI"],
    "Databases": ["SQL"],
    "Programming": ["Python for Data Analysis"],
    "Capabilities": [
        "Data Cleaning",
        "Data Validation",
        "Business Intelligence Reporting",
        "Operational Analytics",
        "Market Analysis",
        "Data Storytelling",
        "Digital Strategy",
        "Training & Facilitation",
    ],
}

# ---------------------------------------------------------------------------
# CV SKILLS (with proficiency % for progress bars)
# ---------------------------------------------------------------------------
CV_SKILLS = [
    {"name": "SQL", "level": 90},
    {"name": "Microsoft Excel", "level": 95},
    {"name": "Power BI", "level": 92},
    {"name": "Data Cleaning", "level": 90},
    {"name": "Reporting Automation", "level": 88},
    {"name": "Business Intelligence", "level": 90},
]

# ---------------------------------------------------------------------------
# EXPERIENCE
# ---------------------------------------------------------------------------
EXPERIENCE = [
    {
        "role": "Digital Consultant & Data Analyst",
        "org": "McMoren Logistics Company",
        "location": "Lagos, Nigeria",
        "dates": "Nov 2020 - Present",
        "description": (
            "Built logistics data frameworks, Excel analytical models, and performance "
            "dashboards that improved reporting accuracy, delivery efficiency, compliance, "
            "and fuel-cost visibility."
        ),
        "highlights": [
            "Designed a data collection framework that improved logistics data accuracy by 35% and reduced reporting delays by 25%.",
            "Developed Excel-based analytical models and performance dashboards to monitor fleet movement and KPIs, enhancing delivery efficiency by 20%.",
            "Integrated traffic and regulatory datasets into internal systems, supporting 100% transport and safety compliance.",
            "Filtered, validated, and automated cleaning for 50,000+ operational records monthly.",
            "Conducted trend and variance analyses that led to a 15% reduction in fuel costs and better route planning.",
        ],
    },
    {
        "role": "Business Analyst",
        "org": "McAdur Imagination Cafe",
        "location": "Lagos, Nigeria",
        "dates": "Aug 2016 - Sept 2019",
        "description": (
            "Collected, cleaned, transformed, and validated multi-country business datasets "
            "to improve reporting accuracy and reveal customer and sales patterns."
        ),
        "highlights": [
            "Collected, cleaned, and transformed multi-country datasets, improving reporting accuracy by 30%.",
            "Corrected data inconsistencies across multiple databases, reducing processing errors by 40% through validation and standardization.",
            "Delivered data-driven reports that influenced strategic decisions and boosted sales performance by 18%.",
        ],
    },
]

# ---------------------------------------------------------------------------
# EDUCATION
# ---------------------------------------------------------------------------
EDUCATION = [
    {
        "degree": "Bachelor of Science in Statistics",
        "institution": "University of Ilorin",
        "location": "Kwara State, Nigeria",
        "year": "2019",
        "gpa": "3.77/5.00",
        "honors": "Second Class Upper",
    },
]

# ---------------------------------------------------------------------------
# CERTIFICATIONS
# ---------------------------------------------------------------------------
CERTIFICATIONS = [
    "Data Analytics and Business Intelligence, Dataleum Academy (May 2023 - June 2023)",
    "SQL Database (Beginner & Intermediate), Sololearn Academy",
    "Python for Data Analysis (Beginner), Sololearn Academy",
    "Data Analytics Essentials, Cisco Networking Academy",
]

LANGUAGES = ["English - Fluent"]

SOFT_SKILLS = [
    "Analytical Thinking",
    "Communication",
    "Problem Solving",
    "Team Collaboration",
    "Attention to Detail",
]

# ---------------------------------------------------------------------------
# SPECIALISATIONS (About page feature cards)
# ---------------------------------------------------------------------------
SPECIALISATIONS = [
    {
        "icon": "graph-up-arrow",
        "title": "Operational Analytics",
        "description": (
            "Logistics and business performance analysis built around accuracy, "
            "cost control, KPI visibility, and decision-ready reporting."
        ),
    },
    {
        "icon": "bar-chart-line-fill",
        "title": "BI Dashboards & Reporting",
        "description": (
            "Excel and Power BI dashboards that help teams monitor performance, "
            "spot variance, and act faster."
        ),
    },
    {
        "icon": "mortarboard-fill",
        "title": "Analytics Training",
        "description": (
            "Practical analytics training across Excel, Power BI, SQL, and data "
            "storytelling for business teams and youth programs."
        ),
    },
]

# ---------------------------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "slug": "customer-laptop-preference-analytics",
        "title": "Customer Laptop Preference Analytics",
        "year": "2025",
        "category": "analysis",
        "description": (
            "PC market survey analytics identifying customer preferences across "
            "10 major laptop brands."
        ),
        "tools": ["Excel", "Power BI"],
        "image": "/assets/images/projects/sales-analysis.jpg",
        "featured": True,
        "links": {},
        "detail": (
            "Conducted PC market survey analytics to identify customer preferences "
            "across 10 major laptop brands. Cleaned, modelled, and visualized survey "
            "data in Excel and Power BI, revealing trends in performance, affordability, "
            "design priorities, buying behavior, and pricing sensitivity."
        ),
    },
    {
        "slug": "hewwelt-data-job-research",
        "title": "Hewwelt Data Job Research",
        "year": "2024",
        "category": "bi-dashboards",
        "description": (
            "SQL and Power BI recruitment analytics for 50,000+ job data entries."
        ),
        "tools": ["SQL", "Power BI"],
        "image": "/assets/images/projects/sql-supply-chain.jpg",
        "featured": True,
        "links": {},
        "detail": (
            "Processed and validated 50,000+ recruitment data entries using SQL, "
            "then designed interactive Power BI dashboards for hiring metrics and "
            "recruitment trends. The work improved HR reporting efficiency by 25% "
            "and produced strategic recommendations for recruitment optimization."
        ),
    },
    {
        "slug": "digprom-analytics",
        "title": "Digprom Analytics",
        "year": "2023",
        "category": "analysis",
        "description": (
            "Customer-record cleaning, ETL preparation, and churn insight reporting."
        ),
        "tools": ["SQL", "Power BI"],
        "image": "/assets/images/projects/mcmoren-dashboard.jpg",
        "featured": True,
        "links": {},
        "detail": (
            "Cleaned and transformed over 100,000 customer records with SQL and "
            "Power BI, improving model readiness by 35%. Designed automated ETL data "
            "pipelines for churn prediction, reducing manual processing time by 40% "
            "and supporting data-driven retention strategies."
        ),
    },
    {
        "slug": "kwara-tech-for-youths-initiative",
        "title": "Kwara Tech for Youths' Initiative",
        "year": "2022",
        "category": "education",
        "description": (
            "Youth empowerment analytics and Excel/Power BI training for 200+ participants."
        ),
        "tools": ["Excel", "Power BI"],
        "image": "/assets/images/projects/midramo-curriculum.jpg",
        "featured": False,
        "links": {},
        "detail": (
            "Collaborated with a state technology office to deliver data-driven youth "
            "empowerment programs, training 200+ participants in Excel and Power BI. "
            "Led analysis on training performance metrics and created dashboards for "
            "government reporting and stakeholder presentations."
        ),
    },
    {
        "slug": "kid-tech-coding-program",
        "title": "Kid Tech Coding Program",
        "year": "2021",
        "category": "education",
        "description": (
            "Analytics modules introducing children aged 8-15 to data storytelling and visualization."
        ),
        "tools": ["Excel", "Power BI"],
        "image": "/assets/images/projects/excel-vba.jpg",
        "featured": False,
        "links": {},
        "detail": (
            "Developed analytics modules for children aged 8-15, simplifying concepts "
            "like data storytelling and Power BI dashboards. Evaluated participant "
            "performance data to improve teaching content and increase learner engagement by 45%."
        ),
    },
]

# ---------------------------------------------------------------------------
# FILTER CATEGORIES for Works
# ---------------------------------------------------------------------------
WORKS_CATEGORIES = [
    ("all", "All"),
    ("analysis", "Data Analysis"),
    ("bi-dashboards", "BI Dashboards"),
    ("education", "Education"),
]

# ---------------------------------------------------------------------------
# VIDEOS
# ---------------------------------------------------------------------------
VIDEOS = [
    {
        "video_id": "dQw4w9WgXcQ",
        "title": "Getting Started with Power BI - A Practical Guide",
        "description": "Build your first interactive dashboard in Power BI from scratch using real business data.",
        "category": "tutorials",
    },
    {
        "video_id": "dQw4w9WgXcQ",
        "title": "SQL for Data Analysts - Core Queries You Must Know",
        "description": "Master SELECT, JOIN, GROUP BY, and window functions with real-world examples.",
        "category": "tutorials",
    },
    {
        "video_id": "dQw4w9WgXcQ",
        "title": "Cleaning Messy Data with Python Pandas",
        "description": "Step-by-step walkthrough of handling nulls, duplicates, type errors, and outliers.",
        "category": "walkthroughs",
    },
    {
        "video_id": "dQw4w9WgXcQ",
        "title": "How I Built a Logistics Dashboard",
        "description": "A behind-the-scenes case study on Power BI dashboard design for logistics.",
        "category": "case-studies",
    },
]

# ---------------------------------------------------------------------------
# VIDEO FILTER CATEGORIES
# ---------------------------------------------------------------------------
VIDEO_CATEGORIES = [
    ("all", "All"),
    ("tutorials", "Tutorials"),
    ("walkthroughs", "Walkthroughs"),
    ("case-studies", "Case Studies"),
]

# ---------------------------------------------------------------------------
# SOCIAL LINKS (for footer and about page)
# ---------------------------------------------------------------------------
SOCIAL_LINKS = [
    {"icon": "linkedin", "href": "https://linkedin.com/in/banjisegun", "label": "LinkedIn"},
    {"icon": "github", "href": "https://github.com/banjisegun99", "label": "GitHub"},
    {"icon": "envelope-fill", "href": "mailto:banjisegun99@gmail.com", "label": "Email"},
]
