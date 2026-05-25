"""
data.py — All content data for Segun Banji's Data Science Portfolio.
Replace placeholder content (slugs, video IDs, links) with your real data.
"""

# ---------------------------------------------------------------------------
# OWNER
# ---------------------------------------------------------------------------
OWNER = {
    "name": "Segun Banji",
    "initials": "SB",
    "title": "Data Analyst & Business Intelligence Expert",
    "tagline": (
        "7+ years turning raw data into decisions that move businesses forward. "
        "Consultant · Educator · BI Strategist."
    ),
    "email": "banjisegun99@gmail.com",
    "linkedin": "https://linkedin.com/in/banjisegun",
    "github": "https://github.com/banjisegun99",
    "location": "Nigeria",
    "bio": [
        (
            "I am a seasoned Data Analyst and Business Intelligence Expert with over 7 years "
            "of experience transforming complex datasets into clear, actionable insights. "
            "Currently serving as Digital Consultant at McMoren Logistics and Lecturer in Data "
            "Analytics at Midramo Institute, I bridge the gap between raw numbers and real "
            "business outcomes."
        ),
        (
            "My work spans dashboards that track operational performance in real-time, SQL "
            "query pipelines that clean and model messy enterprise data, and Python automation "
            "that saves analysts hours every week. I am equally passionate about education — "
            "designing curriculum that makes analytics accessible to beginners and SME teams."
        ),
    ],
    "how_i_work": (
        "I lead with questions before tools: What decision does this data need to support? "
        "Who reads this report, and how do they think? From there I pick the right stack — "
        "Excel for rapid prototyping, Power BI for stakeholder dashboards, Python for "
        "automation and prediction, SQL for everything in between."
    ),
    "youtube_channel": "#",  # Replace with real YouTube channel URL
    "availability": "Available for consulting",
}

# ---------------------------------------------------------------------------
# STATS (home page)
# ---------------------------------------------------------------------------
STATS = [
    {"value": 50, "suffix": "+", "label": "Projects Completed"},
    {"value": 7, "suffix": "+", "label": "Years Experience"},
    {"value": 200, "suffix": "+", "label": "Students Trained"},
    {"value": 15, "suffix": "+", "label": "Happy Clients"},
]

# ---------------------------------------------------------------------------
# SKILLS (flat list for home skills strip)
# ---------------------------------------------------------------------------
SKILLS_FLAT = [
    "Microsoft Excel", "Power BI", "Google Sheets", "Google Data Studio",
    "SQL", "MySQL", "Microsoft SQL Server", "Python",
    "Pandas", "NumPy", "Matplotlib", "VBA",
    "Data Cleaning", "Data Storytelling", "Dashboard Design", "Curriculum Design",
]

# ---------------------------------------------------------------------------
# TOOLS (grouped for About page)
# ---------------------------------------------------------------------------
TOOLS = {
    "Analytics & BI": ["Microsoft Excel", "Power BI", "Google Data Studio", "Google Sheets"],
    "Databases": ["Microsoft SQL Server", "MySQL", "SQL"],
    "Programming": ["Python", "Pandas", "NumPy", "Matplotlib", "VBA"],
    "Capabilities": [
        "Data Cleaning & Transformation",
        "Business Intelligence Reporting",
        "Predictive & Descriptive Analytics",
        "Data Storytelling",
        "SQL Query Optimization",
        "Teaching & Curriculum Design",
    ],
}

# ---------------------------------------------------------------------------
# CV SKILLS (with proficiency % for progress bars)
# ---------------------------------------------------------------------------
CV_SKILLS = [
    {"name": "Power BI", "level": 95},
    {"name": "Microsoft Excel / VBA", "level": 95},
    {"name": "SQL", "level": 88},
    {"name": "Python (Pandas, NumPy)", "level": 80},
    {"name": "Google Data Studio", "level": 85},
    {"name": "Data Storytelling", "level": 92},
]

# ---------------------------------------------------------------------------
# EXPERIENCE
# ---------------------------------------------------------------------------
EXPERIENCE = [
    {
        "role": "Digital Consultant",
        "org": "McMoren Logistics",
        "dates": "2021 – Present",
        "description": (
            "Designed and maintained Power BI dashboards to monitor truck movement, "
            "driver efficiency, and turnaround time. Reduced delivery exception reporting "
            "time by 40% through automated data pipelines."
        ),
    },
    {
        "role": "Data Analytics Lecturer",
        "org": "Midramo Institute",
        "dates": "2020 – Present",
        "description": (
            "Designed and delivered a comprehensive Data Analytics curriculum with "
            "real-world business case studies. Over 200 students trained across cohorts "
            "spanning Excel, SQL, Power BI, and Python."
        ),
    },
    {
        "role": "Data Analyst",
        "org": "Kid Tech Initiative",
        "dates": "2019 – 2020",
        "description": (
            "Introduced young learners to data visualization concepts and Python coding "
            "fundamentals. Developed age-appropriate projects to foster computational thinking."
        ),
    },
]

# ---------------------------------------------------------------------------
# EDUCATION
# ---------------------------------------------------------------------------
EDUCATION = [
    {
        "degree": "B.Sc. Computer Science",
        "institution": "University (Nigeria)",
        "year": "2017",
    },
]

# ---------------------------------------------------------------------------
# CERTIFICATIONS
# ---------------------------------------------------------------------------
CERTIFICATIONS = [
    "Microsoft Certified: Power BI Data Analyst Associate",
    "Google Data Analytics Professional Certificate",
    "SQL for Data Science — Coursera",
    "Python for Everybody — University of Michigan / Coursera",
]

# ---------------------------------------------------------------------------
# SPECIALISATIONS (About page feature cards)
# ---------------------------------------------------------------------------
SPECIALISATIONS = [
    {
        "icon": "graph-up-arrow",
        "title": "Data Analysis & Insights",
        "description": (
            "End-to-end analysis from raw data ingestion through cleaning, modelling, "
            "and insight communication — built for real business decisions."
        ),
    },
    {
        "icon": "bar-chart-line-fill",
        "title": "BI Dashboards & Reporting",
        "description": (
            "Power BI and Excel dashboards that give operations, management, and "
            "executives instant visibility into what matters most."
        ),
    },
    {
        "icon": "mortarboard-fill",
        "title": "Analytics Education",
        "description": (
            "Curriculum design and delivery that takes complete beginners to job-ready "
            "analysts — covering Excel, SQL, Python, and Power BI."
        ),
    },
]

# ---------------------------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "slug": "mcmoren-logistics-dashboard",
        "title": "McMoren Logistics BI Dashboard",
        "category": "bi-dashboards",
        "description": (
            "A live Power BI dashboard suite tracking truck movement, driver efficiency, "
            "fuel consumption, and delivery turnaround time across the entire fleet. "
            "Enabled management to cut report generation time from 2 days to real-time."
        ),
        "tools": ["Power BI", "SQL Server", "Excel"],
        "image": "/assets/images/projects/mcmoren-dashboard.jpg",
        "featured": True,
        "links": {},
        "detail": (
            "The McMoren Logistics dashboard project began with a data audit of three "
            "disconnected Excel workbooks and a partially maintained SQL Server database. "
            "After normalising the schema and building an ETL pipeline, we created a "
            "five-page Power BI report covering fleet overview, driver performance, route "
            "efficiency, fuel KPIs, and an executive summary. The dashboard refreshes "
            "automatically every hour via scheduled data gateway."
        ),
    },
    {
        "slug": "midramo-analytics-curriculum",
        "title": "Midramo Analytics Curriculum",
        "category": "education",
        "description": (
            "A structured 12-week Data Analytics course designed for Midramo Institute, "
            "covering Excel fundamentals, SQL querying, Power BI dashboarding, and an "
            "introduction to Python data analysis."
        ),
        "tools": ["Excel", "SQL", "Power BI", "Python"],
        "image": "/assets/images/projects/midramo-curriculum.jpg",
        "featured": True,
        "links": {},
        "detail": (
            "Designed from scratch as a competency-based curriculum with weekly practical "
            "business case studies. Each module includes a dataset, guided exercises, and "
            "a mini-project that mirrors real analyst workflows. Over 200 students have "
            "completed the programme across multiple cohorts."
        ),
    },
    {
        "slug": "sales-performance-analysis",
        "title": "Sales Performance Analysis",
        "category": "analysis",
        "description": (
            "Deep-dive Excel and Python analysis of 3-year sales data for an SME client. "
            "Identified seasonality patterns, top-performing product lines, and "
            "underperforming regions with actionable recommendations."
        ),
        "tools": ["Python", "Pandas", "Matplotlib", "Excel"],
        "image": "/assets/images/projects/sales-analysis.jpg",
        "featured": False,
        "links": {},
        "detail": (
            "Starting from raw transactional exports, the data was cleaned and merged "
            "using Pandas before exploratory analysis. Seasonality decomposition revealed "
            "a consistent Q3 dip that had previously been attributed to market conditions "
            "but was actually a supply-chain lag. Recommendations led to a 12% revenue "
            "improvement in the following quarter."
        ),
    },
    {
        "slug": "hr-attrition-model",
        "title": "HR Attrition Prediction Model",
        "category": "analysis",
        "description": (
            "A Python-based predictive model to identify employees at high risk of "
            "attrition, built on HR survey data and performance records."
        ),
        "tools": ["Python", "Pandas", "NumPy", "Scikit-learn", "Matplotlib"],
        "image": "/assets/images/projects/hr-attrition.jpg",
        "featured": False,
        "links": {},
        "detail": (
            "Cleaned and feature-engineered 1,400-row HR dataset. Logistic regression "
            "and random forest models were compared; the final model achieved 87% accuracy "
            "on a hold-out test set. Results were visualised in a Matplotlib report handed "
            "to HR leadership for proactive retention planning."
        ),
    },
    {
        "slug": "sql-supply-chain-optimisation",
        "title": "Supply Chain SQL Optimisation",
        "category": "analysis",
        "description": (
            "Rewrote legacy stored procedures and introduced indexed views across a "
            "retail client's SQL Server database, cutting key query execution times by up to 70%."
        ),
        "tools": ["SQL Server", "SQL", "Power BI"],
        "image": "/assets/images/projects/sql-supply-chain.jpg",
        "featured": False,
        "links": {},
        "detail": (
            "The client's ERP reporting module was timing out on monthly stock-reconciliation "
            "queries. After profiling execution plans we added composite indexes, rewrote "
            "correlated sub-queries as CTEs, and introduced incremental refresh for Power BI "
            "reports. Monthly reporting runtime dropped from 45 minutes to under 4 minutes."
        ),
    },
    {
        "slug": "excel-vba-automation",
        "title": "Excel VBA Reporting Automation",
        "category": "bi-dashboards",
        "description": (
            "Automated a multi-step weekly reporting workflow for a financial services firm "
            "using Excel VBA macros, saving the team 6+ hours per week."
        ),
        "tools": ["Excel", "VBA"],
        "image": "/assets/images/projects/excel-vba.jpg",
        "featured": False,
        "links": {},
        "detail": (
            "The existing workflow required an analyst to manually copy data from six source "
            "files, apply formatting, and email a summary to 12 stakeholders. VBA macros "
            "now handle the entire process — data merge, formatting, chart refresh, and "
            "Outlook email dispatch — at the click of a button."
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
        "video_id": "dQw4w9WgXcQ",  # Replace with real YouTube video IDs
        "title": "Getting Started with Power BI — A Practical Guide",
        "description": "Build your first interactive dashboard in Power BI from scratch using real business data.",
        "category": "tutorials",
    },
    {
        "video_id": "dQw4w9WgXcQ",
        "title": "SQL for Data Analysts — Core Queries You Must Know",
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
        "title": "How I Built the McMoren Logistics Dashboard",
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
