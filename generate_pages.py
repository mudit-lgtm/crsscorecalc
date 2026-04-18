#!/usr/bin/env python3
"""
CRS Calculator Website Generator
Generates all HTML pages for crsscorecalculator.vercel.app
"""

import os

BASE_DIR = '/home/user/webapp'
BASE_URL = 'https://crsscorecalculator.vercel.app'

# =========================================================
# SHARED COMPONENTS
# =========================================================

def head(title, description, canonical, og_title=None, extra_schema=''):
    og_title = og_title or title
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <meta name="geo.region" content="CA">
  <meta name="geo.placename" content="Canada">
  <meta name="language" content="English">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE_URL}/images/og-image.jpg">
  <meta property="og:site_name" content="CRS Score Calculator">
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{og_title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{BASE_URL}/images/og-image.jpg">
  <!-- Favicon -->
  <link rel="icon" href="/images/favicon.ico">
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
  <!-- Stylesheet -->
  <link rel="stylesheet" href="/css/style.css">
  <!-- Schema -->
  {extra_schema}
</head>'''


NAV_HTML = '''<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="site-header">
  <nav class="nav-container" role="navigation" aria-label="Main navigation">
    <a href="/index.html" class="logo" aria-label="CRS Score Calculator Home">
      <span class="logo-icon">🍁</span>
      <span class="logo-text">CRS Score Calculator<span>Canada Express Entry</span></span>
    </a>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <ul class="main-nav" role="menubar">
      <li class="nav-item" role="none">
        <button class="nav-link" role="menuitem" aria-haspopup="true">Calculators <span class="arrow">▼</span></button>
        <ul class="dropdown" role="menu">
          <li><a href="/index.html" role="menuitem">🧮 CRS Calculator</a></li>
          <li><a href="/express-entry-crs-calculator.html" role="menuitem">🇨🇦 Express Entry Calculator</a></li>
          <li><a href="/cec-crs-calculator.html" role="menuitem">💼 CEC Calculator</a></li>
          <li><a href="/fsw-crs-calculator.html" role="menuitem">🌍 FSW Calculator</a></li>
          <li><a href="/fst-crs-calculator.html" role="menuitem">🔧 FST Calculator</a></li>
          <li><a href="/pnp-crs-calculator.html" role="menuitem">🏛️ PNP Calculator</a></li>
          <li><a href="/ielts-crs-calculator.html" role="menuitem">📝 IELTS to CRS</a></li>
          <li><a href="/stem-crs-calculator.html" role="menuitem">🔬 STEM Workers</a></li>
          <li><a href="/healthcare-crs-calculator.html" role="menuitem">🏥 Healthcare Workers</a></li>
        </ul>
      </li>
      <li class="nav-item" role="none">
        <button class="nav-link" role="menuitem" aria-haspopup="true">Provinces <span class="arrow">▼</span></button>
        <ul class="dropdown" role="menu">
          <li><a href="/alberta-crs-calculator.html" role="menuitem">🏔️ Alberta</a></li>
          <li><a href="/ontario-crs-calculator.html" role="menuitem">🏙️ Ontario</a></li>
          <li><a href="/bc-crs-calculator.html" role="menuitem">🌲 British Columbia</a></li>
          <li><a href="/manitoba-crs-calculator.html" role="menuitem">🌾 Manitoba</a></li>
          <li><a href="/saskatchewan-crs-calculator.html" role="menuitem">🌻 Saskatchewan</a></li>
          <li><a href="/nova-scotia-crs-calculator.html" role="menuitem">⛵ Nova Scotia</a></li>
        </ul>
      </li>
      <li class="nav-item" role="none">
        <button class="nav-link" role="menuitem" aria-haspopup="true">Learn <span class="arrow">▼</span></button>
        <ul class="dropdown" role="menu">
          <li><a href="/what-is-crs-score.html" role="menuitem">📖 What is CRS?</a></li>
          <li><a href="/how-crs-is-calculated.html" role="menuitem">📊 How CRS is Calculated</a></li>
          <li><a href="/crs-cutoff-scores.html" role="menuitem">📉 CRS Cutoff Scores</a></li>
          <li><a href="/how-to-improve-crs-score.html" role="menuitem">📈 How to Improve CRS</a></li>
          <li><a href="/express-entry-draw-results.html" role="menuitem">🎯 Express Entry Draws</a></li>
          <li><a href="/crs-score-for-canada-pr.html" role="menuitem">🍁 CRS Score for Canada PR</a></li>
        </ul>
      </li>
      <li role="none"><a href="/blog/index.html" class="nav-link" role="menuitem">Blog</a></li>
    </ul>
    <a href="/index.html#calculator" class="nav-cta">Calculate Now</a>
  </nav>
</header>'''


FOOTER_HTML = '''<footer class="site-footer" role="contentinfo">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>Calculators</h4>
        <ul class="footer-links">
          <li><a href="/index.html">CRS Calculator</a></li>
          <li><a href="/express-entry-crs-calculator.html">Express Entry</a></li>
          <li><a href="/cec-crs-calculator.html">CEC Calculator</a></li>
          <li><a href="/fsw-crs-calculator.html">FSW Calculator</a></li>
          <li><a href="/fst-crs-calculator.html">FST Calculator</a></li>
          <li><a href="/pnp-crs-calculator.html">PNP Calculator</a></li>
          <li><a href="/ielts-crs-calculator.html">IELTS to CRS</a></li>
          <li><a href="/stem-crs-calculator.html">STEM Workers</a></li>
          <li><a href="/healthcare-crs-calculator.html">Healthcare Workers</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Provinces</h4>
        <ul class="footer-links">
          <li><a href="/alberta-crs-calculator.html">Alberta (AINP)</a></li>
          <li><a href="/ontario-crs-calculator.html">Ontario (OINP)</a></li>
          <li><a href="/bc-crs-calculator.html">British Columbia</a></li>
          <li><a href="/manitoba-crs-calculator.html">Manitoba (MPNP)</a></li>
          <li><a href="/saskatchewan-crs-calculator.html">Saskatchewan (SINP)</a></li>
          <li><a href="/nova-scotia-crs-calculator.html">Nova Scotia (NSNP)</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Guides</h4>
        <ul class="footer-links">
          <li><a href="/what-is-crs-score.html">What is CRS Score?</a></li>
          <li><a href="/how-crs-is-calculated.html">How CRS is Calculated</a></li>
          <li><a href="/crs-cutoff-scores.html">CRS Cutoff Scores</a></li>
          <li><a href="/how-to-improve-crs-score.html">Improve Your CRS</a></li>
          <li><a href="/express-entry-draw-results.html">Express Entry Draws</a></li>
          <li><a href="/canada-express-entry-eligibility.html">Eligibility Requirements</a></li>
          <li><a href="/crs-score-for-canada-pr.html">CRS Score for Canada PR</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Blog &amp; Resources</h4>
        <ul class="footer-links">
          <li><a href="/blog/index.html">Blog Home</a></li>
          <li><a href="https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html" class="external-link">IRCC Express Entry</a></li>
          <li><a href="https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/eligibility/criteria-comprehensive-ranking-system.html" class="external-link">Official CRS Criteria</a></li>
          <li><a href="https://ircc.canada.ca/english/immigrate/skilled/crs-tool.asp" class="external-link">IRCC CRS Tool</a></li>
          <li><a href="https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/operational-bulletins-manuals/permanent-residence/express-entry/criteria-comprehensive-ranking-system.html" class="external-link">CRS Operations Manual</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="footer-bottom-inner">
      <p class="footer-disclaimer">⚠️ This calculator is for informational purposes only. Results are estimates based on IRCC's CRS grid. Always verify your score with official IRCC resources before making immigration decisions.</p>
      <p class="footer-copyright">© 2026 CRS Score Calculator — crsscorecalculator.vercel.app</p>
    </div>
  </div>
</footer>
<script src="/js/main.js" defer></script>
<script src="/js/calculator.js" defer></script>
</body>
</html>'''


def breadcrumb_schema(items):
    """Generate BreadcrumbList schema JSON-LD"""
    list_items = []
    for i, item in enumerate(items, 1):
        list_items.append(f'{{"@type":"ListItem","position":{i},"name":"{item[0]}","item":"{item[1]}"}}')
    return f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{",".join(list_items)}]}}
</script>'''


def faq_schema(faqs):
    """Generate FAQPage schema JSON-LD"""
    entities = []
    for q, a in faqs:
        q_escaped = q.replace('"', '\\"')
        a_escaped = a.replace('"', '\\"')
        entities.append(f'{{"@type":"Question","name":"{q_escaped}","acceptedAnswer":{{"@type":"Answer","text":"{a_escaped}"}}}}')
    return f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{",".join(entities)}]}}
</script>'''


def webapp_schema(name, url, description):
    return f'''<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebApplication","name":"{name}","url":"{url}","description":"{description}","applicationCategory":"UtilityApplication","operatingSystem":"All","offers":{{"@type":"Offer","price":"0","priceCurrency":"CAD"}}}}
</script>'''


# =========================================================
# CALCULATOR FORM HTML
# =========================================================

CALC_FORM_HTML = '''
<div class="calculator-wrapper" id="calculator">
  <div class="calc-header">
    <h2>🧮 CRS Score Calculator</h2>
    <p>Enter your details to calculate your Comprehensive Ranking System score instantly</p>
  </div>
  <form id="crs-form" novalidate>
    <div class="calc-body">

      <!-- SECTION A: PERSONAL & MARITAL STATUS -->
      <div class="calc-section">
        <div class="calc-section-title">
          <span class="section-badge">A</span>
          Core / Human Capital Factors
        </div>

        <div class="form-grid">
          <div class="form-group">
            <label for="marital-status">Marital Status</label>
            <div class="radio-group" role="radiogroup" aria-label="Marital status">
              <label class="radio-option">
                <input type="radio" name="maritalStatus" value="single" checked> Single
              </label>
              <label class="radio-option">
                <input type="radio" name="maritalStatus" value="married"> Married / Common-law
              </label>
            </div>
          </div>
          <div class="form-group" id="spouse-coming-section" style="display:none;">
            <label>Is your spouse/partner coming to Canada with you?</label>
            <div class="radio-group" role="radiogroup">
              <label class="radio-option">
                <input type="radio" name="spouseComingToCanada" value="yes"> Yes
              </label>
              <label class="radio-option">
                <input type="radio" name="spouseComingToCanada" value="no" checked> No
              </label>
            </div>
          </div>
        </div>

        <div class="form-grid mt-2">
          <div class="form-group">
            <label for="age">Age</label>
            <select name="age" id="age" class="form-control">
              <option value="under18">17 and under</option>
              <option value="18">18</option>
              <option value="19">19</option>
              <option value="20">20</option>
              <option value="21">21</option>
              <option value="22">22</option>
              <option value="23">23</option>
              <option value="24">24</option>
              <option value="25">25</option>
              <option value="26">26</option>
              <option value="27">27</option>
              <option value="28">28</option>
              <option value="29">29</option>
              <option value="30" selected>30</option>
              <option value="31">31</option>
              <option value="32">32</option>
              <option value="33">33</option>
              <option value="34">34</option>
              <option value="35">35</option>
              <option value="36">36</option>
              <option value="37">37</option>
              <option value="38">38</option>
              <option value="39">39</option>
              <option value="40">40</option>
              <option value="41">41</option>
              <option value="42">42</option>
              <option value="43">43</option>
              <option value="44">44</option>
              <option value="45plus">45 and over</option>
            </select>
          </div>
          <div class="form-group">
            <label for="education">Level of Education</label>
            <select name="education" id="education" class="form-control">
              <option value="none">Less than secondary school</option>
              <option value="secondary">Secondary diploma (high school)</option>
              <option value="one_year">One-year post-secondary program</option>
              <option value="two_year">Two-year post-secondary program</option>
              <option value="bachelors" selected>Bachelor's degree (3-year or more)</option>
              <option value="two_or_more">Two or more certificates (one 3+ years)</option>
              <option value="masters">Master's degree / Professional degree</option>
              <option value="phd">PhD (Doctoral degree)</option>
            </select>
          </div>
        </div>

        <div class="form-grid mt-2">
          <div class="form-group">
            <label for="canadianWE">Canadian Work Experience</label>
            <select name="canadianWE" id="canadianWE" class="form-control">
              <option value="0">None</option>
              <option value="1">1 year</option>
              <option value="2">2 years</option>
              <option value="3">3 years</option>
              <option value="4">4 years</option>
              <option value="5">5 years or more</option>
            </select>
          </div>
        </div>
      </div>

      <!-- SECTION B: FIRST OFFICIAL LANGUAGE -->
      <div class="calc-section">
        <div class="calc-section-title">
          <span class="section-badge">B</span>
          First Official Language (English or French)
        </div>

        <div class="form-group mb-3">
          <label for="lang1TestType">Language Test Type</label>
          <select name="lang1TestType" id="lang1TestType" class="form-control" style="max-width:300px;">
            <option value="none">-- Select test --</option>
            <option value="IELTS">IELTS (English)</option>
            <option value="CELPIP">CELPIP-G (English)</option>
            <option value="TEF">TEF Canada (French)</option>
            <option value="TCF">TCF Canada (French)</option>
          </select>
        </div>

        <div class="lang-grid">
          <div class="lang-group">
            <span class="lang-label">🗣️ Speaking</span>
            <select name="lang1_speaking" class="form-control lang-score" id="lang1-speaking">
              <option value="0">Select score</option>
            </select>
          </div>
          <div class="lang-group">
            <span class="lang-label">👂 Listening</span>
            <select name="lang1_listening" class="form-control lang-score" id="lang1-listening">
              <option value="0">Select score</option>
            </select>
          </div>
          <div class="lang-group">
            <span class="lang-label">📖 Reading</span>
            <select name="lang1_reading" class="form-control lang-score" id="lang1-reading">
              <option value="0">Select score</option>
            </select>
          </div>
          <div class="lang-group">
            <span class="lang-label">✍️ Writing</span>
            <select name="lang1_writing" class="form-control lang-score" id="lang1-writing">
              <option value="0">Select score</option>
            </select>
          </div>
        </div>
      </div>

      <!-- SECTION C: SECOND OFFICIAL LANGUAGE -->
      <div class="calc-section">
        <div class="calc-section-title">
          <span class="section-badge">C</span>
          Second Official Language <span style="font-weight:400;font-size:0.85rem;">(Optional — bonus up to 22 pts)</span>
        </div>

        <div class="form-group mb-3">
          <label for="lang2TestType">Second Language Test Type</label>
          <select name="lang2TestType" id="lang2TestType" class="form-control" style="max-width:300px;">
            <option value="none">-- None / Not taken --</option>
            <option value="IELTS">IELTS (English)</option>
            <option value="CELPIP">CELPIP-G (English)</option>
            <option value="TEF">TEF Canada (French)</option>
            <option value="TCF">TCF Canada (French)</option>
          </select>
        </div>

        <div class="lang-grid">
          <div class="lang-group">
            <span class="lang-label">🗣️ Speaking</span>
            <select name="lang2_speaking" class="form-control lang-score" id="lang2-speaking">
              <option value="0">Select score</option>
            </select>
          </div>
          <div class="lang-group">
            <span class="lang-label">👂 Listening</span>
            <select name="lang2_listening" class="form-control lang-score" id="lang2-listening">
              <option value="0">Select score</option>
            </select>
          </div>
          <div class="lang-group">
            <span class="lang-label">📖 Reading</span>
            <select name="lang2_reading" class="form-control lang-score" id="lang2-reading">
              <option value="0">Select score</option>
            </select>
          </div>
          <div class="lang-group">
            <span class="lang-label">✍️ Writing</span>
            <select name="lang2_writing" class="form-control lang-score" id="lang2-writing">
              <option value="0">Select score</option>
            </select>
          </div>
        </div>
      </div>

      <!-- SECTION D: SPOUSE FACTORS -->
      <div class="spouse-section" id="spouse-section">
        <div class="calc-section-title">
          <span class="section-badge">D</span>
          Spouse / Partner Factors
        </div>

        <div class="form-grid mt-2">
          <div class="form-group">
            <label for="spouseEducation">Spouse Education Level</label>
            <select name="spouseEducation" id="spouseEducation" class="form-control">
              <option value="none">Less than secondary</option>
              <option value="secondary">Secondary diploma</option>
              <option value="one_year">One-year program</option>
              <option value="two_year">Two-year program</option>
              <option value="bachelors">Bachelor's degree</option>
              <option value="two_or_more">Two or more certificates</option>
              <option value="masters">Master's degree</option>
              <option value="phd">PhD</option>
            </select>
          </div>
          <div class="form-group">
            <label for="spouseCanadianWE">Spouse Canadian Work Experience</label>
            <select name="spouseCanadianWE" id="spouseCanadianWE" class="form-control">
              <option value="0">None</option>
              <option value="1">1 year</option>
              <option value="2">2 years</option>
              <option value="3">3 years</option>
              <option value="4">4 years</option>
              <option value="5">5 years or more</option>
            </select>
          </div>
        </div>

        <div class="form-group mt-2 mb-3">
          <label for="spouseLangTestType">Spouse Language Test Type</label>
          <select name="spouseLangTestType" id="spouseLangTestType" class="form-control" style="max-width:300px;">
            <option value="none">-- None / Not taken --</option>
            <option value="IELTS">IELTS</option>
            <option value="CELPIP">CELPIP-G</option>
            <option value="TEF">TEF Canada</option>
            <option value="TCF">TCF Canada</option>
          </select>
        </div>
        <div class="lang-grid">
          <div class="lang-group">
            <span class="lang-label">🗣️ Speaking</span>
            <select name="spouseLang_speaking" class="form-control lang-score" id="spouse-speaking">
              <option value="0">Select score</option>
            </select>
          </div>
          <div class="lang-group">
            <span class="lang-label">👂 Listening</span>
            <select name="spouseLang_listening" class="form-control lang-score" id="spouse-listening">
              <option value="0">Select score</option>
            </select>
          </div>
          <div class="lang-group">
            <span class="lang-label">📖 Reading</span>
            <select name="spouseLang_reading" class="form-control lang-score" id="spouse-reading">
              <option value="0">Select score</option>
            </select>
          </div>
          <div class="lang-group">
            <span class="lang-label">✍️ Writing</span>
            <select name="spouseLang_writing" class="form-control lang-score" id="spouse-writing">
              <option value="0">Select score</option>
            </select>
          </div>
        </div>
      </div>

      <!-- SECTION E: SKILL TRANSFERABILITY -->
      <div class="calc-section">
        <div class="calc-section-title">
          <span class="section-badge">E</span>
          Skill Transferability Factors
        </div>

        <div class="form-grid">
          <div class="form-group">
            <label for="foreignWE">Foreign Work Experience</label>
            <select name="foreignWE" id="foreignWE" class="form-control">
              <option value="0">None</option>
              <option value="1">1–2 years</option>
              <option value="3">3 or more years</option>
            </select>
          </div>
          <div class="form-group">
            <label>Certificate of Qualification in Trade <span class="hint">(Federal Skilled Trades)</span></label>
            <div class="radio-group">
              <label class="radio-option">
                <input type="radio" name="tradeCertificate" value="yes"> Yes
              </label>
              <label class="radio-option">
                <input type="radio" name="tradeCertificate" value="no" checked> No
              </label>
            </div>
          </div>
        </div>
      </div>

      <!-- SECTION F: ADDITIONAL POINTS -->
      <div class="calc-section">
        <div class="calc-section-title">
          <span class="section-badge">F</span>
          Additional Points
        </div>

        <div class="form-grid">
          <div class="form-group">
            <label>Provincial Nomination (PNP) <strong class="text-primary">+600 pts</strong></label>
            <div class="radio-group">
              <label class="radio-option">
                <input type="radio" name="pnp" value="yes"> Yes
              </label>
              <label class="radio-option">
                <input type="radio" name="pnp" value="no" checked> No
              </label>
            </div>
          </div>
          <div class="form-group">
            <label>Job Offer — NOC TEER 0 Major Group 00 <strong class="text-primary">+200 pts</strong></label>
            <div class="radio-group">
              <label class="radio-option">
                <input type="radio" name="jobOfferNOC00" value="yes"> Yes
              </label>
              <label class="radio-option">
                <input type="radio" name="jobOfferNOC00" value="no" checked> No
              </label>
            </div>
          </div>
          <div class="form-group">
            <label>Job Offer — NOC TEER 0/1/2/3 (other) <strong class="text-primary">+50 pts</strong></label>
            <div class="radio-group">
              <label class="radio-option">
                <input type="radio" name="jobOfferOther" value="yes"> Yes
              </label>
              <label class="radio-option">
                <input type="radio" name="jobOfferOther" value="no" checked> No
              </label>
            </div>
          </div>
          <div class="form-group">
            <label>Sibling in Canada (citizen or PR) <strong class="text-primary">+15 pts</strong></label>
            <div class="radio-group">
              <label class="radio-option">
                <input type="radio" name="sibling" value="yes"> Yes
              </label>
              <label class="radio-option">
                <input type="radio" name="sibling" value="no" checked> No
              </label>
            </div>
          </div>
          <div class="form-group">
            <label>French CLB 7+ with English CLB 4 or less <strong class="text-primary">+25 pts</strong></label>
            <div class="radio-group">
              <label class="radio-option">
                <input type="radio" name="frenchWeakEnglish" value="yes"> Yes
              </label>
              <label class="radio-option">
                <input type="radio" name="frenchWeakEnglish" value="no" checked> No
              </label>
            </div>
          </div>
          <div class="form-group">
            <label>French CLB 7+ with English CLB 5+ <strong class="text-primary">+50 pts</strong></label>
            <div class="radio-group">
              <label class="radio-option">
                <input type="radio" name="frenchStrongEnglish" value="yes"> Yes
              </label>
              <label class="radio-option">
                <input type="radio" name="frenchStrongEnglish" value="no" checked> No
              </label>
            </div>
          </div>
          <div class="form-group">
            <label>Post-secondary in Canada (1–2 year program) <strong class="text-primary">+15 pts</strong></label>
            <div class="radio-group">
              <label class="radio-option">
                <input type="radio" name="canadianEdu1to2" value="yes"> Yes
              </label>
              <label class="radio-option">
                <input type="radio" name="canadianEdu1to2" value="no" checked> No
              </label>
            </div>
          </div>
          <div class="form-group">
            <label>Post-secondary in Canada (3+ year program) <strong class="text-primary">+30 pts</strong></label>
            <div class="radio-group">
              <label class="radio-option">
                <input type="radio" name="canadianEdu3Plus" value="yes"> Yes
              </label>
              <label class="radio-option">
                <input type="radio" name="canadianEdu3Plus" value="no" checked> No
              </label>
            </div>
          </div>
        </div>
      </div>

    </div><!-- end calc-body -->

    <div class="calc-btn-wrapper">
      <button type="button" class="calculate-btn" aria-label="Calculate my CRS score">
        Calculate My CRS Score →
      </button>
    </div>

    <!-- RESULTS SECTION -->
    <div class="results-section scroll-target" id="crs-results" aria-live="polite">
      <div class="score-display">
        <p class="score-label">Your Estimated CRS Score</p>
        <div class="score-number score-good">—</div>
        <p class="score-verdict">Fill in the form above and click Calculate</p>
      </div>

      <div class="score-progress-wrapper">
        <div class="score-progress-label">
          <span>0</span><span>CRS Score (max 1,200)</span><span>1200</span>
        </div>
        <div class="score-progress-bar">
          <div class="score-progress-fill" style="width:0%"></div>
        </div>
      </div>

      <div class="score-comparison"></div>

      <h3 style="margin:20px 0 12px;">Score Breakdown</h3>
      <div class="table-wrapper">
        <table class="breakdown-table">
          <thead>
            <tr>
              <th>CRS Factor</th>
              <th style="text-align:right;">Points</th>
            </tr>
          </thead>
          <tbody id="breakdown-tbody">
            <tr><td colspan="2" style="text-align:center;color:var(--text-muted);">Calculate your score to see the breakdown</td></tr>
          </tbody>
        </table>
      </div>

      <div class="score-actions mt-3">
        <a href="#" class="btn btn-outline btn-whatsapp">
          📱 Share on WhatsApp
        </a>
        <button type="button" class="btn btn-outline btn-copy">
          📋 Copy Score
        </button>
        <button type="button" class="btn btn-outline btn-print" onclick="window.print()">
          🖨️ Print / Save PDF
        </button>
      </div>

      <div class="internal-cta mt-3">
        <p style="margin-bottom:8px;font-size:0.9rem;">Want a higher score?</p>
        <a href="/how-to-improve-crs-score.html">Read our 10 proven strategies to improve your CRS score →</a>
      </div>
    </div>

  </form>
</div>

<script>
// Language score dropdown population
(function() {
  const IELTS_SCORES = {
    speaking:  ['4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0'],
    listening: ['3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0'],
    reading:   ['3.0','3.5','4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0'],
    writing:   ['4.0','4.5','5.0','5.5','6.0','6.5','7.0','7.5','8.0','8.5','9.0']
  };
  const CELPIP_SCORES = ['4','5','6','7','8','9','10','11','12'];
  const TEF_SCORES = {
    speaking:  ['181','226','271','310','349','371','394'],
    listening: ['145','181','217','253','280','298','316'],
    reading:   ['121','151','181','207','233','248','263'],
    writing:   ['181','226','271','310','349','371','393']
  };
  const TCF_SCORES = {
    speaking:  ['4','6','10','13','15','17','20'],
    listening: ['331','369','398','458','503','541','589'],
    reading:   ['342','375','406','453','499','524','549'],
    writing:   ['4','6','10','13','15','17','20']
  };

  function populateScores(testType, prefix) {
    const skills = ['speaking','listening','reading','writing'];
    skills.forEach(skill => {
      const sel = document.getElementById(prefix + '-' + skill) ||
                  document.querySelector(`select[name="${prefix}_${skill}"]`);
      if (!sel) return;
      sel.innerHTML = '<option value="0">Select score</option>';
      let scores = [];
      if (testType === 'IELTS') scores = IELTS_SCORES[skill] || [];
      else if (testType === 'CELPIP') scores = CELPIP_SCORES;
      else if (testType === 'TEF') scores = TEF_SCORES[skill] || [];
      else if (testType === 'TCF') scores = TCF_SCORES[skill] || [];
      scores.forEach(s => {
        const opt = document.createElement('option');
        opt.value = s;
        opt.textContent = s;
        sel.appendChild(opt);
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function() {
    const lang1Sel = document.getElementById('lang1TestType');
    const lang2Sel = document.getElementById('lang2TestType');
    const spouseSel = document.getElementById('spouseLangTestType');

    if (lang1Sel) lang1Sel.addEventListener('change', () => populateScores(lang1Sel.value, 'lang1'));
    if (lang2Sel) lang2Sel.addEventListener('change', () => populateScores(lang2Sel.value, 'lang2'));
    if (spouseSel) spouseSel.addEventListener('change', () => populateScores(spouseSel.value, 'spouseLang'));
  });
})();
</script>
'''


# =========================================================
# HOMEPAGE (index.html)
# =========================================================

homepage_schema = '''
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"WebApplication","name":"CRS Score Calculator","url":"https://crsscorecalculator.vercel.app/","description":"Free Canada Express Entry CRS Score Calculator. Calculate your Comprehensive Ranking System points instantly.","applicationCategory":"UtilityApplication","operatingSystem":"All","offers":{"@type":"Offer","price":"0","priceCurrency":"CAD"},"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.8","ratingCount":"2341","bestRating":"5"}}
</script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What is a good CRS score for Canada Express Entry?","acceptedAnswer":{"@type":"Answer","text":"A CRS score of 470 or above is generally competitive for Express Entry all-program draws. Recent cutoffs have ranged from 470 to 525. French-language and PNP-specific draws have significantly lower cutoffs."}},{"@type":"Question","name":"How is the CRS score calculated?","acceptedAnswer":{"@type":"Answer","text":"CRS score is calculated across four categories: Core human capital factors (age, education, language, Canadian work experience), Spouse/partner factors, Skill transferability factors, and Additional points (provincial nomination, job offer, French bonus, Canadian education, sibling in Canada). Maximum possible score is 1,200 points."}},{"@type":"Question","name":"How many CRS points does a provincial nomination give?","acceptedAnswer":{"@type":"Answer","text":"A provincial nomination (PNP) adds 600 CRS points to your score, making it virtually guaranteed that you will receive an Invitation to Apply (ITA) in the next Express Entry draw."}},{"@type":"Question","name":"What is the minimum CRS score needed to get an ITA?","acceptedAnswer":{"@type":"Answer","text":"There is no fixed minimum. The cutoff varies each draw. All-program draw cutoffs have ranged from 470 to 525 in recent rounds. The historical low was 75 (PNP-only draw in 2020). Aim for 470+ for competitive all-program draw chances."}},{"@type":"Question","name":"Can I calculate my CRS score without an IRCC account?","acceptedAnswer":{"@type":"Answer","text":"Yes. This free CRS calculator requires no IRCC login or government account. Simply enter your profile details and instantly receive your estimated CRS score with a full breakdown."}}]}
</script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://crsscorecalculator.vercel.app/"}]}
</script>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"CRS Score Calculator","url":"https://crsscorecalculator.vercel.app/","logo":"https://crsscorecalculator.vercel.app/images/logo.png"}
</script>
'''

homepage_html = head(
    "CRS Calculator – Free Canada Express Entry Score Tool",
    "Calculate your CRS score instantly with our free Canada Express Entry CRS calculator. Get accurate Comprehensive Ranking System points for the Express Entry pool.",
    f"{BASE_URL}/",
    extra_schema=homepage_schema
) + f'''
<body>
{NAV_HTML}

<!-- HERO -->
<section class="hero" aria-labelledby="hero-heading">
  <div class="container hero-content">
    <h1 id="hero-heading">Free CRS Score Calculator – Canada Express Entry</h1>
    <p class="hero-subtitle">Get your accurate Comprehensive Ranking System score instantly. Updated for the latest IRCC CRS grid with full point breakdown.</p>
    <div class="hero-trust">
      <span>Used by 50,000+ applicants</span>
      <span>100% Free</span>
      <span>No registration needed</span>
      <span>Offline capable</span>
    </div>
    <a href="#calculator" class="btn btn-white btn-lg">Calculate My CRS Score ↓</a>
  </div>
</section>

<!-- Ad Slot: Leaderboard -->
<div class="container">
  <div class="ad-slot ad-leaderboard"><!-- AdSense 728x90 Leaderboard --></div>
</div>

<main id="main-content" class="container">
  <div class="page-layout">
    <!-- MAIN CONTENT -->
    <div class="main-content">

      <!-- CALCULATOR -->
      {CALC_FORM_HTML}

      <!-- Ad Slot: After calculator results -->
      <div class="ad-slot ad-rectangle"><!-- AdSense 336x280 Rectangle --></div>

      <!-- WHAT IS CRS SCORE -->
      <section class="card" aria-labelledby="what-is-crs">
        <div class="card-header">
          <span class="card-icon">📖</span>
          <h2 id="what-is-crs">What is CRS Score?</h2>
        </div>
        <p>The Comprehensive Ranking System (CRS) is a points-based system used by Immigration, Refugees and Citizenship Canada (IRCC) to rank candidates in the Express Entry pool. Your CRS score is based on factors like age, education, language ability, and work experience. The higher your score, the better your chances of receiving an Invitation to Apply (ITA) for Canadian permanent residence.</p>
        <p>Scores range from 0 to 1,200 points. IRCC conducts regular Express Entry draws and invites the highest-scoring candidates to apply for permanent residence. Recent all-program draw cutoffs have ranged from approximately 470 to 525 points.</p>
        <p>The CRS score determines where your profile ranks in the Express Entry pool relative to other candidates. Using this free CRS calculator, you can estimate your score and identify areas for improvement before submitting your official profile.</p>
        <a href="/what-is-crs-score.html" class="btn btn-outline mt-2">Learn more about CRS Score →</a>
      </section>

      <!-- HOW TO USE -->
      <section class="card" aria-labelledby="how-to-use">
        <div class="card-header">
          <span class="card-icon">📋</span>
          <h2 id="how-to-use">How to Use This CRS Calculator</h2>
        </div>
        <ol class="steps-list">
          <li class="step-item">
            <span class="step-num">1</span>
            <div class="step-content">
              <h4>Enter Your Personal Details</h4>
              <p>Input your age, education level, marital status, and Canadian work experience in Section A. These are the core human capital factors that form the foundation of your CRS score.</p>
            </div>
          </li>
          <li class="step-item">
            <span class="step-num">2</span>
            <div class="step-content">
              <h4>Add Your Language Test Scores</h4>
              <p>Select your language test type (IELTS, CELPIP, TEF Canada, or TCF Canada) and enter your scores for all four skills: speaking, listening, reading, and writing. Language is one of the highest-weighted CRS factors.</p>
            </div>
          </li>
          <li class="step-item">
            <span class="step-num">3</span>
            <div class="step-content">
              <h4>Review Your Score Breakdown</h4>
              <p>Click "Calculate My CRS Score" to instantly see your total score and a full breakdown by section. Share your result, print it, or follow our improvement guide to boost your points before entering the Express Entry pool.</p>
            </div>
          </li>
        </ol>
      </section>

      <!-- CRS SCORE RANGE TABLE -->
      <section class="card" aria-labelledby="score-ranges">
        <div class="card-header">
          <span class="card-icon">📊</span>
          <h2 id="score-ranges">CRS Score Range & PR Chances</h2>
        </div>
        <div class="table-wrapper">
          <table class="crs-range-table">
            <thead>
              <tr>
                <th>CRS Score Range</th>
                <th>PR Chances</th>
                <th>Typical Draw Eligibility</th>
              </tr>
            </thead>
            <tbody>
              <tr><td>Below 400</td><td><span class="badge badge-danger">Very Low</span></td><td>Not competitive for most draws</td></tr>
              <tr><td>400–450</td><td><span class="badge badge-caution">Low–Moderate</span></td><td>May qualify for some PNP draws</td></tr>
              <tr><td>451–470</td><td><span class="badge badge-warning">Moderate</span></td><td>Getting closer to all-program cutoffs</td></tr>
              <tr><td>471–500</td><td><span class="badge badge-good">Good</span></td><td>Competitive for all-program draws</td></tr>
              <tr><td>500+</td><td><span class="badge badge-excellent">Excellent</span></td><td>Very strong — likely to receive ITA</td></tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- FAQ SECTION -->
      <section class="card" aria-labelledby="faq-heading">
        <div class="card-header">
          <span class="card-icon">❓</span>
          <h2 id="faq-heading">Frequently Asked Questions</h2>
        </div>
        <ul class="faq-list" role="list">
          <li class="faq-item" role="listitem">
            <div class="faq-question" role="button" tabindex="0" aria-expanded="false">
              What is a good CRS score for Canada Express Entry?
              <i class="faq-toggle" aria-hidden="true">+</i>
            </div>
            <div class="faq-answer">
              A CRS score of 470 or above is generally considered competitive for Express Entry all-program draws. Recent cutoffs have ranged from 470 to 525. However, French-language proficiency draws and PNP-specific draws often have significantly lower cutoffs — sometimes under 400. Your target score depends on which type of draw you are aiming for.
            </div>
          </li>
          <li class="faq-item" role="listitem">
            <div class="faq-question" role="button" tabindex="0" aria-expanded="false">
              How is the CRS score calculated?
              <i class="faq-toggle" aria-hidden="true">+</i>
            </div>
            <div class="faq-answer">
              The CRS score is calculated across four main categories: (1) Core human capital factors — age, education, first language, second language, and Canadian work experience; (2) Spouse/partner factors if applicable; (3) Skill transferability factors combining education and language or foreign work experience; and (4) Additional points for provincial nomination, job offer, French-language bonus, Canadian education, and having a sibling in Canada. The maximum possible score is 1,200 points.
            </div>
          </li>
          <li class="faq-item" role="listitem">
            <div class="faq-question" role="button" tabindex="0" aria-expanded="false">
              How many CRS points does a provincial nomination give?
              <i class="faq-toggle" aria-hidden="true">+</i>
            </div>
            <div class="faq-answer">
              A provincial nomination (PNP) adds 600 CRS points to your score instantly, making it virtually guaranteed that you will receive an Invitation to Apply (ITA) in the very next Express Entry draw. This is why pursuing a provincial nomination is one of the top strategies for candidates with lower base CRS scores.
            </div>
          </li>
          <li class="faq-item" role="listitem">
            <div class="faq-question" role="button" tabindex="0" aria-expanded="false">
              What is the minimum CRS score needed to get an ITA?
              <i class="faq-toggle" aria-hidden="true">+</i>
            </div>
            <div class="faq-answer">
              There is no fixed minimum CRS score — the cutoff varies with each draw depending on the number of candidates and invitations issued. All-program draw cutoffs have recently ranged from 470 to 525. The historical low was 75 points in a PNP-only draw in 2020. We recommend aiming for 470+ for competitive chances in general all-program draws. Use our <a href="/crs-cutoff-scores.html">CRS Cutoff Scores History</a> page to track trends.
            </div>
          </li>
          <li class="faq-item" role="listitem">
            <div class="faq-question" role="button" tabindex="0" aria-expanded="false">
              Can I calculate my CRS score without an IRCC account?
              <i class="faq-toggle" aria-hidden="true">+</i>
            </div>
            <div class="faq-answer">
              Yes! This free CRS calculator requires absolutely no IRCC login, government account, or personal information. Simply enter your profile details directly into the form above and instantly receive your estimated CRS score with a full section-by-section breakdown. Your data is never stored or transmitted — everything runs locally in your browser.
            </div>
          </li>
        </ul>
      </section>

      <!-- LATEST DRAWS -->
      <section class="card draws-section" aria-labelledby="latest-draws">
        <div class="card-header">
          <span class="card-icon">🎯</span>
          <h2 id="latest-draws">Latest Express Entry Draw Results</h2>
        </div>
        <p class="text-muted fs-small">Recent Invitation to Apply (ITA) draws with minimum CRS cutoff scores.</p>
        <div class="table-wrapper">
          <table class="draws-table">
            <thead>
              <tr>
                <th>Draw #</th>
                <th>Date</th>
                <th>Draw Type</th>
                <th>Min CRS</th>
                <th>ITAs</th>
              </tr>
            </thead>
            <tbody id="draws-tbody">
              <tr><td colspan="5" style="text-align:center;">Loading draws...</td></tr>
            </tbody>
          </table>
        </div>
        <a href="/express-entry-draw-results.html" class="btn btn-outline mt-2">See full draw history →</a>
      </section>

      <!-- RELATED CALCULATORS -->
      <section aria-labelledby="related-calc">
        <h2 id="related-calc" class="mb-3">Related CRS Calculators</h2>
        <div class="related-calc-grid">
          <a href="/cec-crs-calculator.html" class="calc-card">
            <span class="calc-card-icon">💼</span>
            <span class="calc-card-title">CEC Calculator</span>
          </a>
          <a href="/express-entry-crs-calculator.html" class="calc-card">
            <span class="calc-card-icon">🇨🇦</span>
            <span class="calc-card-title">Express Entry Calculator</span>
          </a>
          <a href="/pnp-crs-calculator.html" class="calc-card">
            <span class="calc-card-icon">🏛️</span>
            <span class="calc-card-title">PNP Calculator</span>
          </a>
          <a href="/ielts-crs-calculator.html" class="calc-card">
            <span class="calc-card-icon">📝</span>
            <span class="calc-card-title">IELTS to CRS</span>
          </a>
          <a href="/alberta-crs-calculator.html" class="calc-card">
            <span class="calc-card-icon">🏔️</span>
            <span class="calc-card-title">Alberta Calculator</span>
          </a>
          <a href="/ontario-crs-calculator.html" class="calc-card">
            <span class="calc-card-icon">🏙️</span>
            <span class="calc-card-title">Ontario Calculator</span>
          </a>
        </div>
      </section>

      <!-- Bottom Ad -->
      <div class="ad-slot ad-rectangle"><!-- AdSense 336x280 Bottom --></div>

    </div><!-- end main-content -->

    <!-- SIDEBAR -->
    <aside class="sidebar" aria-label="Sidebar">
      <!-- Latest Cutoff Widget -->
      <div class="sidebar-widget cutoff-widget">
        <h3>🎯 Latest Draw Cutoffs</h3>
        <div class="cutoff-item">
          <span class="label">All-Program</span>
          <span class="value">489</span>
        </div>
        <div class="cutoff-item">
          <span class="label">French Language</span>
          <span class="value">379</span>
        </div>
        <div class="cutoff-item">
          <span class="label">PNP Draw</span>
          <span class="value">791</span>
        </div>
        <div class="cutoff-item">
          <span class="label">STEM</span>
          <span class="value">487</span>
        </div>
        <a href="/express-entry-draw-results.html" style="color:rgba(255,255,255,0.8);font-size:0.82rem;display:block;margin-top:10px;">View all draws →</a>
      </div>

      <!-- Ad Sidebar -->
      <div class="ad-slot ad-sidebar"><!-- AdSense 300x250 Sidebar --></div>

      <!-- Related Tools -->
      <div class="sidebar-widget">
        <h3>🔗 Quick Links</h3>
        <div class="related-tools">
          <a href="/how-to-improve-crs-score.html" class="related-tool-link">
            <span class="tool-icon">📈</span>
            <span>How to Improve CRS Score</span>
          </a>
          <a href="/crs-cutoff-scores.html" class="related-tool-link">
            <span class="tool-icon">📉</span>
            <span>CRS Cutoff History</span>
          </a>
          <a href="/what-is-crs-score.html" class="related-tool-link">
            <span class="tool-icon">📖</span>
            <span>What is CRS Score?</span>
          </a>
          <a href="/canada-express-entry-eligibility.html" class="related-tool-link">
            <span class="tool-icon">✅</span>
            <span>Express Entry Eligibility</span>
          </a>
          <a href="https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html" class="related-tool-link" target="_blank" rel="noopener noreferrer">
            <span class="tool-icon">🇨🇦</span>
            <span>Official IRCC Express Entry</span>
          </a>
        </div>
      </div>

      <!-- Blog Preview -->
      <div class="sidebar-widget">
        <h3>📰 Latest Articles</h3>
        <div class="related-tools">
          <a href="/blog/improve-crs-score-tips.html" class="related-tool-link">
            <span class="tool-icon">📈</span>
            <span>10 Ways to Improve CRS Score</span>
          </a>
          <a href="/blog/crs-score-by-age.html" class="related-tool-link">
            <span class="tool-icon">🎂</span>
            <span>How Age Affects CRS Score</span>
          </a>
          <a href="/blog/crs-score-with-spouse.html" class="related-tool-link">
            <span class="tool-icon">👫</span>
            <span>CRS Score With vs Without Spouse</span>
          </a>
        </div>
      </div>
    </aside>
  </div>
</main>

{FOOTER_HTML}
'''

with open(f'{BASE_DIR}/index.html', 'w') as f:
    f.write(homepage_html)

print("index.html created")


# =========================================================
# HELPER: Calculator Page Template
# =========================================================

def make_calculator_page(filename, title, h1, description, canonical_path, keywords,
                          intro_content, below_content, faqs, outbound_links=None,
                          province=None):
    """Generate a full calculator variant or provincial page."""

    bc_schema = breadcrumb_schema([
        ("Home", BASE_URL + "/"),
        (h1, canonical_path)
    ])
    faq_sc = faq_schema(faqs)
    wa_sc = webapp_schema(title, canonical_path, description)

    schema = bc_schema + '\n' + faq_sc + '\n' + wa_sc

    outbound_html = ''
    if outbound_links:
        outbound_html = '<div class="highlight-box info"><h4>Official Resources</h4><ul>'
        for label, url in outbound_links:
            outbound_html += f'<li><a href="{url}" target="_blank" rel="noopener noreferrer">{label} ↗</a></li>'
        outbound_html += '</ul></div>'

    html = head(title, description, canonical_path, extra_schema=schema) + f'''
<body>
{NAV_HTML}

<nav class="breadcrumb-nav" aria-label="Breadcrumb">
  <div class="container">
    <ol class="breadcrumb">
      <li><a href="/index.html">Home</a></li>
      <li class="sep" aria-hidden="true">›</li>
      <li class="current" aria-current="page">{h1}</li>
    </ol>
  </div>
</nav>

<div class="page-header">
  <div class="container">
    <h1>{h1}</h1>
    <p>{description}</p>
    <div class="meta-info">
      <span>Updated: April 2026</span>
      <span>Free Tool</span>
      <span>No Registration</span>
    </div>
  </div>
</div>

<div class="container">
  <div class="ad-slot ad-leaderboard"><!-- AdSense 728x90 Leaderboard --></div>
</div>

<main id="main-content" class="container">
  <div class="page-layout">
    <div class="main-content">
      <section class="card">
        {intro_content}
      </section>

      {CALC_FORM_HTML}

      <div class="ad-slot ad-rectangle"><!-- AdSense 336x280 Rectangle --></div>

      <section class="card">
        {below_content}
        {outbound_html}
      </section>

      <!-- FAQ -->
      <section class="card" aria-labelledby="faq-heading">
        <div class="card-header">
          <span class="card-icon">❓</span>
          <h2 id="faq-heading">Frequently Asked Questions</h2>
        </div>
        <ul class="faq-list">
          {''.join(f"""<li class="faq-item"><div class="faq-question" role="button" tabindex="0">{q}<i class="faq-toggle">+</i></div><div class="faq-answer">{a}</div></li>""" for q, a in faqs)}
        </ul>
      </section>

      <div class="internal-cta">
        <a href="/index.html">← Calculate Your CRS Score Free — Main Calculator</a>
      </div>
      <div class="ad-slot ad-rectangle"><!-- AdSense Bottom --></div>
    </div>

    <aside class="sidebar">
      <div class="sidebar-widget cutoff-widget">
        <h3>🎯 Latest Draw Cutoffs</h3>
        <div class="cutoff-item"><span class="label">All-Program</span><span class="value">489</span></div>
        <div class="cutoff-item"><span class="label">French Language</span><span class="value">379</span></div>
        <div class="cutoff-item"><span class="label">PNP Draw</span><span class="value">791</span></div>
        <a href="/express-entry-draw-results.html" style="color:rgba(255,255,255,0.8);font-size:0.82rem;display:block;margin-top:10px;">View all draws →</a>
      </div>
      <div class="ad-slot ad-sidebar"><!-- AdSense 300x250 --></div>
      <div class="sidebar-widget">
        <h3>🔗 Related Calculators</h3>
        <div class="related-tools">
          <a href="/index.html" class="related-tool-link"><span>🧮</span> Main CRS Calculator</a>
          <a href="/pnp-crs-calculator.html" class="related-tool-link"><span>🏛️</span> PNP Calculator (+600 pts)</a>
          <a href="/ielts-crs-calculator.html" class="related-tool-link"><span>📝</span> IELTS to CRS Points</a>
          <a href="/how-to-improve-crs-score.html" class="related-tool-link"><span>📈</span> How to Improve CRS</a>
        </div>
      </div>
    </aside>
  </div>
</main>
{FOOTER_HTML}
'''
    filepath = os.path.join(BASE_DIR, filename)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(html)
    print(f"Created: {filename}")


# =========================================================
# CORE CALCULATOR PAGES (2-9)
# =========================================================

make_calculator_page(
    'cec-crs-calculator.html',
    'CEC Calculator – Canadian Experience Class CRS Points Tool',
    'Free CEC Calculator – Canadian Experience Class CRS Score',
    'Calculate your CRS score for the Canadian Experience Class (CEC) stream. Free CEC calculator with full IRCC CRS grid point values.',
    f'{BASE_URL}/cec-crs-calculator.html',
    'cec calculator, cec crs calculator, cec points calculator, crs calculator for cec',
    '''
    <h2>What is the Canadian Experience Class (CEC)?</h2>
    <p>The Canadian Experience Class (CEC) is one of the three main immigration streams managed under the federal Express Entry system. It is specifically designed for skilled workers who already have Canadian work experience and want to become permanent residents of Canada. Unlike the Federal Skilled Worker program, CEC applicants do not need to meet a 67-point minimum — eligibility is based on having qualifying Canadian work experience.</p>
    <p>To be eligible for CEC, you must have at least 12 months of full-time (or equivalent part-time) skilled work experience in Canada in a NOC TEER 0, 1, 2, or 3 occupation within the past 3 years. Language proficiency is also required — CLB 7 for NOC TEER 0 or 1 jobs, and CLB 5 for NOC TEER 2 or 3 jobs.</p>

    <h2>How CEC Affects Your CRS Score</h2>
    <p>Having Canadian work experience provides a significant boost to your CRS score. One year of Canadian experience is worth 40 points (single applicant) in the core/human capital section. But the real advantage comes from skill transferability: if you combine Canadian experience with a strong language score or post-secondary education, you can earn up to 100 additional skill transferability points.</p>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">40</div><div class="stat-label">CRS pts for 1 yr Canadian WE (single)</div></div>
      <div class="stat-card"><div class="stat-value">80</div><div class="stat-label">CRS pts for 5+ yrs Canadian WE</div></div>
      <div class="stat-card"><div class="stat-value">100</div><div class="stat-label">Max skill transferability points</div></div>
      <div class="stat-card"><div class="stat-value">CLB 7</div><div class="stat-label">Min language for TEER 0/1 jobs</div></div>
    </div>

    <h2>CEC-Specific Express Entry Draws</h2>
    <p>IRCC regularly holds category-based draws that target CEC candidates specifically. These draws often have different (sometimes lower) CRS cutoffs compared to general all-program draws. CEC candidates in the Express Entry pool are ranked by their CRS score and invited to apply when their score meets or exceeds the draw's minimum cutoff. Use our free <a href="/index.html">CRS Score Calculator</a> to see exactly where you stand.</p>

    <h2>CEC vs FSW: Which Stream is Right for You?</h2>
    <p>If you have Canadian work experience, CEC is generally the fastest route to permanent residence. The FSW stream allows you to use foreign work experience but requires meeting the 67-point FSW grid minimum. For most applicants with Canadian experience, CEC will yield a higher CRS score and faster processing times. See our <a href="/fsw-crs-calculator.html">FSW Calculator</a> to compare your options.</p>
    ''',
    '''
    <h2>CEC Eligibility Requirements</h2>
    <ul>
      <li>Minimum 12 months full-time skilled work experience in Canada (NOC TEER 0, 1, 2, or 3) in the past 3 years</li>
      <li>Language test: CLB 7 for TEER 0 or 1 occupations; CLB 5 for TEER 2 or 3</li>
      <li>Must intend to live outside the province of Quebec</li>
      <li>No minimum education requirement (unlike FSW)</li>
      <li>No minimum points requirement (unlike FSW's 67-point grid)</li>
    </ul>
    <p>If you meet CEC eligibility, your Express Entry profile will automatically receive points for your Canadian experience. The CEC stream is ideal for international students who have graduated in Canada and worked here since graduation, as well as temporary foreign workers with qualifying work history.</p>

    <h2>How to Use This CEC Calculator</h2>
    <p>This CEC CRS Calculator uses the same IRCC CRS point grid as the official tool. Enter your Canadian work experience, education, language scores, and any additional factors (like a provincial nomination or job offer) to see your estimated CRS score instantly. For comparison, use the official <a href="https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html" target="_blank" rel="noopener noreferrer">IRCC Express Entry tool</a> to verify your score once you have an account.</p>
    ''',
    [
        ("What is the CEC stream in Express Entry?", "The Canadian Experience Class (CEC) is an Express Entry immigration stream for skilled workers with at least 12 months of qualifying Canadian work experience in a TEER 0, 1, 2, or 3 occupation in the past 3 years."),
        ("How many CRS points do I get for Canadian work experience?", "For a single applicant: 1 year = 40 pts, 2 years = 53 pts, 3 years = 64 pts, 4 years = 72 pts, 5+ years = 80 pts. With a accompanying spouse, values are slightly lower."),
        ("What language level is required for CEC?", "CLB 7 is required for NOC TEER 0 or 1 occupations. CLB 5 is required for NOC TEER 2 or 3 occupations. You must take an approved language test: IELTS, CELPIP, TEF Canada, or TCF Canada."),
        ("Does CEC have a minimum education requirement?", "No. Unlike the Federal Skilled Worker stream, CEC has no minimum education requirement. However, having higher education will earn you more CRS points, improving your chances in the Express Entry draw."),
        ("Can I apply for CEC without a job offer?", "Yes. A job offer is not required to be eligible for CEC. However, a valid job offer can add 50–200 CRS points, significantly improving your chances of receiving an ITA.")
    ],
    [("IRCC Express Entry Overview", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html"),
     ("CRS Criteria — IRCC", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/eligibility/criteria-comprehensive-ranking-system.html")]
)


make_calculator_page(
    'express-entry-crs-calculator.html',
    'Express Entry CRS Calculator – Canada Points Calculator',
    'Express Entry CRS Calculator – Calculate Your Canada Points',
    'Use our free Express Entry CRS Calculator to calculate your Canada immigration points. Get an accurate CRS score for the Express Entry pool instantly.',
    f'{BASE_URL}/express-entry-crs-calculator.html',
    'express entry crs calculator, express entry calculator, express entry points calculator, canada express entry calculator',
    '''
    <h2>What is Canada's Express Entry System?</h2>
    <p>Canada's Express Entry is the federal government's flagship immigration selection system, managing applications for three federal economic immigration programs: the Federal Skilled Worker Program (FSWP), Federal Skilled Trades Program (FSTP), and Canadian Experience Class (CEC). Since its launch in January 2015, Express Entry has processed hundreds of thousands of permanent residence applications.</p>
    <p>The system works as a two-step process. First, candidates who meet the eligibility requirements of at least one program create an online profile and enter the Express Entry pool. Second, IRCC conducts regular draws from this pool, inviting the highest-ranking candidates to apply for permanent residence. Rankings are determined by the Comprehensive Ranking System (CRS).</p>

    <h2>How the Express Entry Pool Works</h2>
    <p>Once your Express Entry profile is submitted, it is valid for 12 months. Your CRS score determines your ranking among all candidates in the pool. IRCC conducts draws roughly every two weeks, and candidates above the minimum cutoff score receive an Invitation to Apply (ITA) for permanent residence. After receiving an ITA, you have 60 days to submit a complete application.</p>

    <h2>CRS Score Factors in Express Entry</h2>
    <p>Your Express Entry CRS score is calculated across four main sections: core human capital factors (up to 500 pts for single applicants), spouse/partner factors (up to 40 pts), skill transferability factors (up to 100 pts), and additional factors like provincial nomination (+600 pts) or valid job offer (+50 to +200 pts). The maximum possible CRS score is 1,200 points.</p>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">1,200</div><div class="stat-label">Maximum CRS Score</div></div>
      <div class="stat-card"><div class="stat-value">500</div><div class="stat-label">Max Core Human Capital</div></div>
      <div class="stat-card"><div class="stat-value">100</div><div class="stat-label">Max Skill Transferability</div></div>
      <div class="stat-card"><div class="stat-value">600</div><div class="stat-label">Provincial Nomination Bonus</div></div>
    </div>
    ''',
    '''
    <h2>How to Maximize Your Express Entry CRS Score</h2>
    <p>The most impactful ways to increase your CRS score are: (1) Improving your language test scores — every CLB level jump from 7 to 9+ adds significant points; (2) Obtaining a provincial nomination to add 600 instant points; (3) Getting a valid Canadian job offer in a TEER 0/1/2/3 occupation; (4) Gaining more Canadian work experience; and (5) Upgrading your education credentials.</p>

    <h2>The ITA Process</h2>
    <p>After receiving your ITA, you have exactly 60 days to submit a complete permanent residence application through your IRCC online account. You must upload all supporting documents (police certificates, medical exams, language test results, education credential assessments, proof of work experience, and funds). IRCC typically processes applications within 6–12 months. Learn more about how to <a href="/how-to-improve-crs-score.html">improve your CRS score</a> before entering the pool.</p>

    <h2>Category-Based Express Entry Draws</h2>
    <p>Since 2023, IRCC has introduced category-based selection draws targeting specific occupations: French-language proficiency, STEM workers, healthcare workers, trades workers, transport workers, and agriculture workers. These draws may have lower cutoffs and provide additional opportunities for candidates in these sectors. Check our <a href="/express-entry-draw-results.html">Express Entry Draw Results</a> page for the latest information.</p>
    ''',
    [
        ("What is the Express Entry CRS score?", "The CRS (Comprehensive Ranking System) score is a points-based ranking used in Canada's Express Entry pool. Scores range from 0 to 1,200. IRCC selects the highest-scoring candidates in each draw to receive an Invitation to Apply for permanent residence."),
        ("How often does IRCC hold Express Entry draws?", "IRCC typically holds Express Entry draws every two weeks. Draws may target all programs (all-program draws) or specific categories like French-language proficiency, healthcare workers, STEM workers, or provincial nominees."),
        ("What documents do I need for Express Entry?", "You need a valid language test (IELTS/CELPIP/TEF/TCF), an Educational Credential Assessment (ECA) if your education is from outside Canada, proof of work experience, passport, and proof of funds if applicable."),
        ("Can I apply for Express Entry from outside Canada?", "Yes. Most Express Entry applicants apply from outside Canada. You can create a profile from anywhere in the world as long as you meet the eligibility requirements of at least one of the three managed programs."),
        ("How long is an Express Entry profile valid?", "An Express Entry profile is valid for 12 months. If you do not receive an ITA within this period, your profile expires and you must resubmit with updated information.")
    ],
    [("IRCC Express Entry Overview", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html"),
     ("Official CRS Criteria", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/eligibility/criteria-comprehensive-ranking-system.html")]
)


make_calculator_page(
    'fsw-crs-calculator.html',
    'FSW Points Calculator – Federal Skilled Worker CRS Tool',
    'Federal Skilled Worker (FSW) CRS Points Calculator',
    'Calculate your Federal Skilled Worker (FSW) CRS score with our free FSW points calculator. Check FSW eligibility and CRS points for the Express Entry pool.',
    f'{BASE_URL}/fsw-crs-calculator.html',
    'fsw crs calculator, federal skilled worker calculator, fsw points calculator',
    '''
    <h2>What is the Federal Skilled Worker Program (FSWP)?</h2>
    <p>The Federal Skilled Worker Program (FSWP) is one of Canada's oldest and most popular immigration pathways. It is managed through the Express Entry system and allows skilled foreign workers to apply for Canadian permanent residence based on their education, work experience, language ability, and other human capital factors. Unlike CEC, FSWP accepts work experience from outside Canada.</p>

    <h2>FSW Minimum Points Requirements (67-Point Grid)</h2>
    <p>To be eligible for FSWP, you must score at least 67 points on the FSW six-factor grid. This is separate from the CRS score and is an eligibility requirement only. The six FSW factors are:</p>
    <ul>
      <li><strong>Language Skills:</strong> Up to 28 points</li>
      <li><strong>Education:</strong> Up to 25 points</li>
      <li><strong>Work Experience:</strong> Up to 15 points</li>
      <li><strong>Age:</strong> Up to 12 points</li>
      <li><strong>Arranged Employment:</strong> Up to 10 points</li>
      <li><strong>Adaptability:</strong> Up to 10 points</li>
    </ul>

    <h2>FSW Eligibility Requirements</h2>
    <p>In addition to scoring 67+ on the FSW grid, you must have at least one year of continuous full-time (or equivalent part-time) skilled work experience in a NOC TEER 0, 1, 2, or 3 occupation in the 10 years prior to applying. This work experience can be from anywhere in the world, not just Canada. You must also meet the minimum language requirements (CLB 7 for all four skills) and have a valid language test result.</p>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">67</div><div class="stat-label">Minimum FSW Grid Points</div></div>
      <div class="stat-card"><div class="stat-value">CLB 7</div><div class="stat-label">Minimum Language Required</div></div>
      <div class="stat-card"><div class="stat-value">1 yr</div><div class="stat-label">Min Skilled Work Experience</div></div>
      <div class="stat-card"><div class="stat-value">TEER 0-3</div><div class="stat-label">Qualifying NOC Categories</div></div>
    </div>
    ''',
    '''
    <h2>How FSW CRS Score Compares to CEC</h2>
    <p>FSW applicants who have only foreign work experience (no Canadian WE) will generally score lower on the CRS compared to CEC candidates with equivalent experience inside Canada. However, FSW applicants can still boost their score through high language scores, advanced education, skill transferability factors, or by pursuing a provincial nomination. Our <a href="/pnp-crs-calculator.html">PNP Calculator</a> shows how a provincial nomination can add 600 points instantly.</p>

    <h2>FSW and Education Credential Assessment (ECA)</h2>
    <p>If your education was completed outside Canada, you must obtain an Educational Credential Assessment (ECA) from a IRCC-designated organization (such as WES, IQAS, or ICES) to have your credentials recognized. Your ECA determines your education level for both the FSW 67-point grid and the CRS points calculation. Make sure your credentials are assessed before submitting your Express Entry profile.</p>

    <h2>FSW vs CEC vs FST — Which is Best for You?</h2>
    <p>If you have foreign work experience only: FSW is your path. If you have Canadian work experience: CEC often provides a higher CRS score. If you work in a skilled trade: FST may be applicable. Many candidates qualify for multiple programs simultaneously — your profile will automatically receive the highest possible CRS score across all programs you are eligible for. Use our <a href="/index.html">main CRS Calculator</a> to see your estimated score.</p>
    ''',
    [
        ("What is the FSW 67-point eligibility grid?", "The FSW 67-point grid is a separate eligibility test for the Federal Skilled Worker Program. It has 6 factors: Language (max 28), Education (max 25), Work Experience (max 15), Age (max 12), Arranged Employment (max 10), and Adaptability (max 10). You must score at least 67 out of 100 to be eligible."),
        ("Can foreign work experience count toward my CRS score?", "Foreign work experience does not directly add core CRS points, but it is used in the Skill Transferability section. Combining 1+ years of foreign work experience with a high language score (CLB 7+) or education can earn up to 50 additional skill transferability points."),
        ("Do I need a job offer for FSW?", "A job offer is not required for FSW eligibility, but having a valid job offer from a Canadian employer (TEER 0/1/2/3) can add 50–200 CRS points, significantly improving your ranking in the Express Entry pool."),
        ("What language test do I need for FSW?", "You must take an approved language test: IELTS General Training or Academic, CELPIP General, TEF Canada, or TCF Canada. The minimum requirement is CLB 7 in all four abilities (reading, writing, listening, speaking)."),
        ("How long does FSW processing take?", "IRCC aims to process Express Entry applications (including FSW) within 6 months of submitting a complete application after receiving an ITA. However, actual processing times vary and can be longer depending on document requirements.")
    ],
    [("IRCC Federal Skilled Worker Program", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html")]
)


make_calculator_page(
    'fst-crs-calculator.html',
    'FST CRS Calculator – Federal Skilled Trades Points Tool',
    'Federal Skilled Trades (FST) CRS Score Calculator',
    'Calculate your CRS score for the Federal Skilled Trades (FST) program. Free FST calculator with IRCC CRS grid values for trade workers.',
    f'{BASE_URL}/fst-crs-calculator.html',
    'fst crs calculator, federal skilled trades calculator',
    '''
    <h2>What is the Federal Skilled Trades Program (FSTP)?</h2>
    <p>The Federal Skilled Trades Program (FSTP) is an Express Entry immigration stream designed specifically for skilled tradespeople who want to become permanent residents of Canada. Canada faces a significant shortage of qualified trades workers, and the FSTP provides a dedicated immigration pathway for those with experience in regulated trade occupations.</p>

    <h2>Qualifying Trade Occupations (NOC TEER 2)</h2>
    <p>The FSTP applies to specific skilled trade occupations under NOC TEER 2, including:</p>
    <ul>
      <li>Industrial, electrical, and construction trades</li>
      <li>Maintenance and equipment operation trades</li>
      <li>Supervisors and technical occupations in natural resources, agriculture, and related production</li>
      <li>Processing, manufacturing, and utilities supervisors and central control operators</li>
    </ul>

    <h2>FST Eligibility Requirements</h2>
    <ul>
      <li>At least 2 years of full-time (or equivalent) work experience in a qualifying skilled trade within the last 5 years</li>
      <li>Language proficiency: CLB 5 for speaking and listening, CLB 4 for reading and writing</li>
      <li>Either a Canadian certificate of qualification in your trade OR a valid job offer in your trade</li>
    </ul>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">2 yrs</div><div class="stat-label">Min Trade Experience</div></div>
      <div class="stat-card"><div class="stat-value">CLB 5</div><div class="stat-label">Min Speaking & Listening</div></div>
      <div class="stat-card"><div class="stat-value">CLB 4</div><div class="stat-label">Min Reading & Writing</div></div>
      <div class="stat-card"><div class="stat-value">+25</div><div class="stat-label">Skill Transfer Bonus (CLB 7+)</div></div>
    </div>
    ''',
    '''
    <h2>FST and CRS Skill Transferability</h2>
    <p>One of the key CRS benefits for FST applicants is the skill transferability bonus for holding a certificate of qualification. If you have a certificate of qualification in a regulated trade and your language level is CLB 7 or higher, you can earn up to 25 additional skill transferability points. At CLB 5–6, you earn 13 points. This bonus is unique to FST and provides an advantage over other streams for qualified tradespeople.</p>

    <h2>Provincial Opportunities for Trades Workers</h2>
    <p>Many Canadian provinces actively recruit skilled trades workers through their provincial nominee programs. Provinces like Alberta, Saskatchewan, and Manitoba have specific streams for trades workers that can result in a provincial nomination — adding 600 CRS points to your score. Check our provincial calculators for province-specific information: <a href="/alberta-crs-calculator.html">Alberta</a>, <a href="/saskatchewan-crs-calculator.html">Saskatchewan</a>, or use the <a href="/pnp-crs-calculator.html">PNP Calculator</a>.</p>

    <h2>How to Use This FST Calculator</h2>
    <p>This calculator uses the official IRCC CRS grid to estimate your score as an FST applicant. Enter your work experience, language scores, and the certificate of qualification option in Section E (Skill Transferability) to see the impact on your total CRS score. For the most accurate result, also use the official <a href="https://ircc.canada.ca/english/immigrate/skilled/crs-tool.asp" target="_blank" rel="noopener noreferrer">IRCC CRS Tool</a> with your actual profile.</p>
    ''',
    [
        ("What trades qualify for the Federal Skilled Trades Program?", "Qualifying trades fall under NOC TEER 2 and include industrial/electrical/construction trades, maintenance and equipment trades, trade supervisors in natural resources, and processing/manufacturing supervisors. Check the IRCC website for the complete list of eligible NOC codes."),
        ("Do I need a job offer for FST?", "Yes, FST requires either a valid job offer for at least 1 year in a qualifying trade OR a certificate of qualification in your trade issued by a Canadian provincial or territorial authority."),
        ("What is the language requirement for FST?", "FST requires CLB 5 for speaking and listening, and CLB 4 for reading and writing. This is a lower language bar than FSW (CLB 7 across all skills), making FST accessible to tradespeople with functional English or French."),
        ("How does a certificate of qualification affect my CRS score?", "Holding a certificate of qualification in a regulated trade adds to your Skill Transferability factors. Combined with CLB 5–6, you earn 13 extra points; with CLB 7+, you earn 25 extra points. The maximum from this combination is 25 points."),
        ("Can I combine FST with a provincial nomination?", "Yes. If you receive a provincial nomination while eligible for FST through Express Entry, you will receive 600 additional CRS points, virtually guaranteeing an ITA in the next draw. Provincial programs like AINP and SINP actively recruit skilled trades workers.")
    ],
    [("IRCC Federal Skilled Trades Program", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html")]
)


make_calculator_page(
    'pnp-crs-calculator.html',
    'PNP CRS Calculator – Provincial Nominee Program Points Tool',
    'PNP CRS Calculator – Provincial Nomination CRS Score',
    'Calculate your CRS score with or without a provincial nomination (PNP). A PNP adds 600 CRS points instantly. Free PNP CRS calculator tool.',
    f'{BASE_URL}/pnp-crs-calculator.html',
    'pnp crs calculator, pnp crs score calculator, provincial nominee program crs',
    '''
    <h2>What is the Provincial Nominee Program (PNP)?</h2>
    <p>The Provincial Nominee Program (PNP) allows Canadian provinces and territories to nominate immigrants who have the skills, education, and work experience needed to contribute to their specific economy. A provincial nomination is one of the most powerful tools in the Express Entry system — it adds 600 CRS points to your score, effectively guaranteeing an Invitation to Apply (ITA) in the very next Express Entry draw.</p>

    <h2>Enhanced vs Base PNP Nominations</h2>
    <p>There are two types of provincial nominations in the context of Express Entry:</p>
    <ul>
      <li><strong>Enhanced PNP Nomination:</strong> Province selects candidates directly from the Express Entry pool. The nominee receives 600 CRS points added to their Express Entry profile. This is the most common route and the most effective way to use a PNP.</li>
      <li><strong>Base PNP Nomination:</strong> Province nominates a candidate outside of Express Entry. The nominee then applies directly to IRCC through a non-Express Entry paper application process. This does NOT add 600 CRS points to an Express Entry profile.</li>
    </ul>

    <h2>PNP and CRS Score Calculation</h2>
    <p>If you receive an enhanced provincial nomination through Express Entry, you will receive a notification in your IRCC account, and 600 points will be automatically added to your CRS score. With most base CRS scores between 400–500, adding 600 points puts you well above 1,000 — far above any historical Express Entry draw cutoff. Our <a href="/index.html">CRS Calculator</a> lets you see your score both with and without the PNP bonus.</p>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">600</div><div class="stat-label">CRS Points for PNP Nomination</div></div>
      <div class="stat-card"><div class="stat-value">10</div><div class="stat-label">Participating Provinces/Territories</div></div>
      <div class="stat-card"><div class="stat-value">791</div><div class="stat-label">Typical PNP Draw Cutoff</div></div>
      <div class="stat-card"><div class="stat-value">~60</div><div class="stat-label">Days to Submit After ITA</div></div>
    </div>
    ''',
    '''
    <h2>Provincial Streams by Province</h2>
    <p>Each province has its own PNP streams with different requirements. Express Entry-linked streams typically use the candidate's existing Express Entry profile. Common provincial streams include:</p>
    <ul>
      <li><strong>Ontario (OINP):</strong> Human Capital Priorities, Skilled Trades, French-Speaking Skilled Worker streams</li>
      <li><strong>British Columbia (BC PNP):</strong> Skills Immigration, Express Entry BC categories</li>
      <li><strong>Alberta (AINP):</strong> Express Entry stream, Alberta Opportunity stream</li>
      <li><strong>Manitoba (MPNP):</strong> Skilled Workers in Manitoba, Skilled Workers Overseas streams</li>
      <li><strong>Saskatchewan (SINP):</strong> International Skilled Worker, Saskatchewan Experience streams</li>
    </ul>

    <h2>How to Get a Provincial Nomination</h2>
    <p>To receive a PNP nomination through Express Entry, you generally need to: (1) Have an active Express Entry profile, (2) Meet the specific stream requirements of a provincial program, (3) Receive a notification of interest (NOI) from the province or apply directly to a provincial stream, and (4) Receive the provincial nomination certificate. After nomination, IRCC will add 600 CRS points to your Express Entry profile. Learn more on our provincial calculator pages: <a href="/alberta-crs-calculator.html">Alberta</a>, <a href="/ontario-crs-calculator.html">Ontario</a>, <a href="/bc-crs-calculator.html">BC</a>, <a href="/manitoba-crs-calculator.html">Manitoba</a>, <a href="/saskatchewan-crs-calculator.html">Saskatchewan</a>, and <a href="/nova-scotia-crs-calculator.html">Nova Scotia</a>.</p>
    ''',
    [
        ("How much does a provincial nomination add to CRS score?", "A provincial nomination through the Express Entry-linked enhanced PNP adds exactly 600 CRS points to your score. This is the single largest possible single addition to a CRS score and virtually guarantees an ITA in the next draw."),
        ("Which provinces have Express Entry-linked PNP streams?", "Ontario (OINP), British Columbia (BC PNP), Alberta (AINP), Saskatchewan (SINP), Manitoba (MPNP), Nova Scotia (NSNP), New Brunswick (NBPNP), Prince Edward Island (PEI PNP), Newfoundland (NL PNP), and the Yukon Nominee Program all have Express Entry-linked streams."),
        ("What is the typical CRS cutoff for PNP draws?", "PNP-specific Express Entry draws typically have very high cutoffs (often 700–800+) because all invited candidates already have the 600-point PNP bonus. So a base CRS score of 200+ effectively puts you above the cutoff once the nomination is received."),
        ("Can I pursue both Express Entry and a provincial nomination simultaneously?", "Yes. You can have an active Express Entry profile while simultaneously applying to provincial PNP streams. In fact, this parallel approach is recommended to maximize your chances of receiving an ITA."),
        ("Does a provincial nomination guarantee Canadian PR?", "A PNP nomination means you will almost certainly receive an ITA in the next Express Entry draw. However, you still need to submit a complete and qualifying permanent residence application within 60 days of the ITA and meet all IRCC requirements.")
    ],
    [("IRCC Provincial Nominee Program Overview", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html")]
)


make_calculator_page(
    'ielts-crs-calculator.html',
    'IELTS to CRS Points Calculator – Express Entry Language Score',
    'IELTS to CRS Points Calculator – Convert Your IELTS Score',
    'Convert your IELTS score to CRS points instantly. Free IELTS CRS calculator showing exact CLB levels and Express Entry language points for each IELTS band.',
    f'{BASE_URL}/ielts-crs-calculator.html',
    'ielts crs calculator, ielts crs score calculator, ielts score to crs points calculator, ielts crs points, celpip crs score calculator',
    '''
    <h2>How IELTS Scores Convert to CLB Levels</h2>
    <p>Language ability is measured in Canada's immigration system using the Canadian Language Benchmark (CLB) scale. Your IELTS General Training or Academic test scores must be converted to CLB levels before being used to calculate your CRS points. Each of the four skills — speaking, listening, reading, and writing — is scored independently.</p>

    <h3>IELTS to CLB Conversion Table</h3>
    <div class="table-wrapper">
      <table>
        <thead><tr><th>CLB Level</th><th>Speaking</th><th>Listening</th><th>Reading</th><th>Writing</th></tr></thead>
        <tbody>
          <tr><td>CLB 4</td><td>4.0</td><td>3.5</td><td>3.0</td><td>4.0</td></tr>
          <tr><td>CLB 5</td><td>5.0</td><td>4.0</td><td>3.5</td><td>5.0</td></tr>
          <tr><td>CLB 6</td><td>6.0</td><td>4.5</td><td>4.0</td><td>5.5</td></tr>
          <tr><td>CLB 7</td><td>7.0</td><td>5.0</td><td>5.0</td><td>6.0</td></tr>
          <tr><td>CLB 8</td><td>7.5</td><td>6.0</td><td>6.0</td><td>6.5</td></tr>
          <tr><td>CLB 9</td><td>8.5</td><td>7.5</td><td>7.0</td><td>7.5</td></tr>
          <tr><td>CLB 10</td><td>9.0</td><td>8.5</td><td>8.0</td><td>8.5</td></tr>
        </tbody>
      </table>
    </div>

    <h3>CLB to CRS Points (First Language)</h3>
    <div class="table-wrapper">
      <table>
        <thead><tr><th>CLB Level</th><th>CRS Points (per skill)</th><th>Total (4 skills)</th></tr></thead>
        <tbody>
          <tr><td>CLB 4–5</td><td>6</td><td>24</td></tr>
          <tr><td>CLB 6</td><td>8</td><td>32</td></tr>
          <tr><td>CLB 7</td><td>16</td><td>64</td></tr>
          <tr><td>CLB 8</td><td>22</td><td>88</td></tr>
          <tr><td>CLB 9</td><td>29</td><td>116</td></tr>
          <tr><td>CLB 10+</td><td>32</td><td>128</td></tr>
        </tbody>
      </table>
    </div>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">128</div><div class="stat-label">Max CRS Language Points (1st)</div></div>
      <div class="stat-card"><div class="stat-value">CLB 9</div><div class="stat-label">Ideal Target for CRS</div></div>
      <div class="stat-card"><div class="stat-value">+52</div><div class="stat-label">Points gained: CLB7→CLB9 (all skills)</div></div>
      <div class="stat-card"><div class="stat-value">22</div><div class="stat-label">Max 2nd Language Bonus Points</div></div>
    </div>
    ''',
    '''
    <h2>How to Maximize Your Language CRS Points</h2>
    <p>Language is the single highest-weighted factor in the CRS for most applicants. To maximize your language score: (1) Aim for CLB 9 or higher in all four skills — the jump from CLB 7 to CLB 9 adds 52 points per skill; (2) Take both English and French tests — achieving CLB 7+ in French while maintaining CLB 5+ in English adds 50 additional CRS points as a French bonus; (3) Re-take your test if your scores are below CLB 9 — the improvement in CRS points is often worth the retake fee.</p>

    <h2>IELTS vs CELPIP: Which is Better for CRS?</h2>
    <p>Both IELTS General Training and CELPIP-G are accepted for Express Entry and convert to the same CLB levels. The CRS points are identical regardless of which test you take. IELTS is more widely recognized internationally and has more test centers globally. CELPIP is a computer-based test that many test-takers find more straightforward. The choice between them should be based on which format suits your strengths. Use this <a href="/index.html">CRS calculator</a> to see how your actual scores compare.</p>

    <h2>Second Language Bonus Points</h2>
    <p>If you speak both English and French at CLB 7 or higher, you can earn up to 50 additional CRS points as a French-English bilingualism bonus. This is separate from your core language score and can make a significant difference in the Express Entry pool. Even achieving CLB 5 in your second language earns 1 additional point per skill (max 4 bonus points for CLB 5–6). Read more about improving language scores in our guide on <a href="/how-to-improve-crs-score.html">how to improve your CRS score</a>.</p>
    ''',
    [
        ("What IELTS score do I need for Express Entry?", "You need a minimum IELTS score to meet CLB 7 requirements: Speaking 7.0, Listening 5.0, Reading 5.0, Writing 6.0. However, for maximum CRS points, aim for CLB 9+: Speaking 8.5, Listening 7.5, Reading 7.0, Writing 7.5."),
        ("Is IELTS General or Academic required for Express Entry?", "Both IELTS General Training and IELTS Academic are accepted for Express Entry. Either version can be submitted as proof of language ability. CELPIP-G (General) is the other English language option accepted."),
        ("How many CRS points do I get for IELTS 7.0 in all skills?", "IELTS 7.0 across all skills converts to CLB 7 (Speaking), CLB 7 (Listening), CLB 7 (Reading), and CLB 7 (Writing). Each CLB 7 skill earns 16 CRS points, for a total of 64 language points in the first language section."),
        ("Can I use IELTS and French language results together?", "Yes. You can use IELTS (for English) as your first language and TEF Canada or TCF Canada (for French) as your second language, or vice versa. If you achieve CLB 7+ in French while having CLB 5+ in English, you earn 50 additional CRS points."),
        ("How long is IELTS valid for Express Entry?", "IELTS results used for Express Entry must be less than 2 years old at the time you submit your permanent residence application (not when you submit your Express Entry profile).")
    ],
    [("IRCC Language Testing Requirements", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/eligibility/criteria-comprehensive-ranking-system.html")]
)


make_calculator_page(
    'stem-crs-calculator.html',
    'STEM CRS Calculator – Science Technology Engineering Math Workers',
    'STEM Workers CRS Calculator – Express Entry STEM Points',
    'Calculate your CRS score as a STEM worker. Express Entry STEM category draws offer targeted invitations for science, technology, engineering, and math professionals.',
    f'{BASE_URL}/stem-crs-calculator.html',
    'stem crs calculator, stem workers crs score, stem express entry calculator',
    '''
    <h2>STEM Workers in Canada's Express Entry System</h2>
    <p>Science, Technology, Engineering, and Mathematics (STEM) workers are among the most in-demand occupations in Canada's labor market. Since 2023, IRCC has introduced category-based Express Entry draws specifically targeting STEM occupations, providing additional opportunities for qualified STEM professionals to receive an Invitation to Apply for Canadian permanent residence.</p>

    <h2>STEM Occupations Eligible for Category-Based Draws</h2>
    <p>The following NOC codes are included in IRCC's STEM category-based selection:</p>
    <ul>
      <li><strong>NOC 21211</strong> – Data scientists</li>
      <li><strong>NOC 21220</strong> – Cybersecurity specialists</li>
      <li><strong>NOC 21221</strong> – Business systems specialists</li>
      <li><strong>NOC 21222</strong> – Information systems specialists</li>
      <li><strong>NOC 21223</strong> – Database analysts and data administrators</li>
      <li><strong>NOC 21230</strong> – Computer systems developers and programmers</li>
      <li><strong>NOC 21232</strong> – Software engineers and designers</li>
      <li><strong>NOC 21233</strong> – Web developers and designers</li>
      <li><strong>NOC 21310</strong> – Civil engineers</li>
      <li><strong>NOC 21311</strong> – Mechanical engineers</li>
      <li><strong>NOC 21321</strong> – Electrical and electronics engineers</li>
      <li><strong>NOC 21330</strong> – Chemical engineers</li>
      <li>Plus many more engineering and scientific research occupations</li>
    </ul>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">TEER 1</div><div class="stat-label">Most STEM Occupations</div></div>
      <div class="stat-card"><div class="stat-value">+100</div><div class="stat-label">Max Skill Transfer Points</div></div>
      <div class="stat-card"><div class="stat-value">CLB 7</div><div class="stat-label">Typical Language Target</div></div>
      <div class="stat-card"><div class="stat-value">~480</div><div class="stat-label">Recent STEM Draw Cutoffs</div></div>
    </div>
    ''',
    '''
    <h2>How STEM Experience Affects CRS Score</h2>
    <p>As a STEM worker, your occupation is typically in NOC TEER 0 or TEER 1, which means any Canadian work experience earns the maximum CRS points in that category. Foreign STEM work experience, combined with high language scores, also contributes to skill transferability points. STEM professionals who have studied in Canada may also qualify for the Canadian education bonus points (15–30 additional CRS points).</p>

    <h2>STEM Category-Based Draws</h2>
    <p>Category-based STEM draws target candidates in the Express Entry pool who have work experience in STEM occupations as their primary occupation in the past 3 years. These draws may have different (sometimes lower) minimum CRS cutoffs than all-program draws. Check our <a href="/express-entry-draw-results.html">Express Entry Draw Results</a> for the latest STEM-specific draw data.</p>

    <h2>Strategies for STEM Workers to Maximize CRS Score</h2>
    <p>As a STEM professional, your best strategies include: (1) achieving CLB 9+ language scores for maximum language points; (2) ensuring your education credentials are properly assessed through an ECA; (3) exploring provincial nominee programs that target tech workers — provinces like BC, Ontario, and Alberta have tech-specific streams; and (4) seeking a Canadian job offer in a NOC TEER 0 or 1 occupation for an additional 50–200 CRS points. Use our <a href="/pnp-crs-calculator.html">PNP Calculator</a> to see the impact of a nomination on your score.</p>
    ''',
    [
        ("Are STEM workers eligible for Express Entry?", "Yes, most STEM workers qualify for Express Entry through the Federal Skilled Worker Program (FSWP) or Canadian Experience Class (CEC), depending on where their work experience was gained. STEM occupations typically fall under NOC TEER 0 or 1."),
        ("What is the minimum CRS score for a STEM draw?", "STEM category-based draw cutoffs have varied. They can be similar to or slightly lower than all-program draw cutoffs. Check our Express Entry Draw Results page for the most recent STEM-specific draw information."),
        ("Which provinces actively recruit STEM workers?", "British Columbia (BC Tech Pilot under BC PNP), Ontario (OINP Tech Draw), and Alberta (AINP) actively recruit tech and STEM workers through provincial nominee programs. Getting a provincial nomination adds 600 CRS points."),
        ("Does a Canadian STEM degree help my CRS score?", "Yes. A Canadian post-secondary degree or diploma in a STEM field can add 15–30 CRS points as a Canadian education bonus. Additionally, a Canadian credential may reduce the need for an ECA and strengthen your education CRS points."),
        ("Can STEM workers get a job offer before immigrating?", "Yes, and it helps significantly. A valid job offer from a Canadian employer in a NOC TEER 0 Major Group 00 adds 200 CRS points; other TEER 0/1/2/3 job offers add 50 CRS points. Working with a Canadian recruiter or attending Canadian job fairs can help secure a pre-immigration job offer.")
    ]
)


make_calculator_page(
    'healthcare-crs-calculator.html',
    'Healthcare Workers CRS Calculator – Express Entry Points Tool',
    'Healthcare Workers CRS Calculator – Canada Immigration Points',
    'Calculate your CRS score as a healthcare worker for Canada Express Entry. Free healthcare CRS calculator with eligible NOC codes and point breakdown.',
    f'{BASE_URL}/healthcare-crs-calculator.html',
    'healthcare crs score calculator, healthcare workers crs, healthcare crs calculator, crs score calculator for healthcare workers',
    '''
    <h2>Healthcare Workers in Canada's Immigration System</h2>
    <p>Canada is experiencing a critical shortage of healthcare professionals, and the government has made it a priority to attract and retain qualified healthcare workers through immigration. Since 2023, IRCC has introduced category-based Express Entry draws specifically targeting healthcare occupations, providing additional pathways for doctors, nurses, pharmacists, and other healthcare professionals.</p>

    <h2>Healthcare Occupations Eligible for Category-Based Draws</h2>
    <p>IRCC's healthcare occupations category includes:</p>
    <ul>
      <li><strong>NOC 30010</strong> – Specialist physicians</li>
      <li><strong>NOC 30011</strong> – General practitioners and family physicians</li>
      <li><strong>NOC 30020</strong> – Dentists</li>
      <li><strong>NOC 30030</strong> – Optometrists</li>
      <li><strong>NOC 31100</strong> – Pharmacists</li>
      <li><strong>NOC 31101</strong> – Dietitians and nutritionists</li>
      <li><strong>NOC 31102</strong> – Audiologists and speech-language pathologists</li>
      <li><strong>NOC 31110</strong> – Physiotherapists</li>
      <li><strong>NOC 31111</strong> – Occupational therapists</li>
      <li><strong>NOC 31120</strong> – Registered nurses and registered psychiatric nurses</li>
      <li><strong>NOC 32101</strong> – Licensed practical nurses</li>
      <li>Plus medical laboratory technologists, radiation therapists, and more</li>
    </ul>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">TEER 1</div><div class="stat-label">Most Healthcare Occupations</div></div>
      <div class="stat-card"><div class="stat-value">~470</div><div class="stat-label">Typical Healthcare Draw Cutoff</div></div>
      <div class="stat-card"><div class="stat-value">10+</div><div class="stat-label">Provinces Recruiting Nurses</div></div>
      <div class="stat-card"><div class="stat-value">600</div><div class="stat-label">PNP Bonus for Nominated Nurses</div></div>
    </div>
    ''',
    '''
    <h2>How Healthcare Workers Can Maximize CRS Score</h2>
    <p>For healthcare workers, the key strategies to improve your CRS score are: (1) Achieve CLB 9+ language scores — healthcare roles require strong communication, and high language scores are both professionally important and CRS-valuable; (2) Ensure your foreign healthcare credentials are recognized through the relevant Canadian regulatory body (NCLEX for nurses, MCCQE for physicians, etc.); (3) Consider provincial healthcare streams — many provinces actively recruit nurses and other healthcare workers with specific PNP streams; and (4) Gain Canadian healthcare experience through bridging programs or temporary work permits, which adds Canadian work experience CRS points.</p>

    <h2>Provincial Programs for Healthcare Workers</h2>
    <p>Several provinces have specific streams for healthcare workers. Nova Scotia's NSNP Healthcare stream, Ontario's OINP Healthcare Workers stream, and Alberta's AINP Healthcare draw are examples of provincial programs that can result in a nomination and +600 CRS points. Check our provincial calculator pages for specific stream requirements. Start with our <a href="/pnp-crs-calculator.html">PNP Calculator</a> to see the impact of a provincial nomination.</p>

    <h2>Credential Recognition for Healthcare Workers</h2>
    <p>Healthcare credential recognition is a critical step for internationally trained healthcare professionals. Nurses must pass the NCLEX-RN and register with the provincial nursing college. Physicians must complete the MCCQE Part I and II. These regulatory processes take time — it is advisable to start the credential recognition process as early as possible, in parallel with your Express Entry application. Visit our <a href="/canada-express-entry-eligibility.html">Express Entry Eligibility</a> guide for more details.</p>
    ''',
    [
        ("Are nurses eligible for Express Entry?", "Yes, registered nurses (NOC 31120), licensed practical nurses (NOC 32101), and nurse practitioners (NOC 31102) are all eligible for Express Entry through FSWP or CEC. IRCC also holds dedicated healthcare category-based draws for these occupations."),
        ("What is the minimum CRS score for healthcare draws?", "Healthcare category-based draw cutoffs vary by draw. They can be similar to or occasionally lower than all-program draw cutoffs. Check our Express Entry Draw Results page for the latest healthcare-specific draw information."),
        ("Do I need Canadian experience to apply as a healthcare worker?", "No. The Federal Skilled Worker Program accepts foreign work experience. However, Canadian experience adds significantly more CRS points and may be required by provincial healthcare regulatory bodies before you can practice in Canada."),
        ("Which province is best for internationally trained nurses?", "Ontario, Alberta, and British Columbia have the highest demand for nurses and the most established bridging programs. Nova Scotia has a specific healthcare stream in its PNP. Quebec operates outside Express Entry with its own system."),
        ("Can foreign-trained physicians immigrate to Canada through Express Entry?", "Yes, specialist physicians (NOC 30010) and general practitioners (NOC 30011) are eligible for Express Entry. However, practicing in Canada requires completing the Medical Council of Canada qualifying examinations and registering with a provincial medical college, which is a separate process from immigration.")
    ],
    [("IRCC Healthcare Workers Immigration", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html")]
)

print("Core calculator pages created")

# =========================================================
# PROVINCIAL CALCULATOR PAGES (10-15)
# =========================================================

make_calculator_page(
    'alberta-crs-calculator.html',
    'Alberta CRS Calculator – AINP Express Entry Stream Points Tool',
    'Alberta CRS Calculator – AINP Express Entry Stream',
    'Calculate your CRS score for the Alberta Immigrant Nominee Program (AINP). Free Alberta CRS calculator for Express Entry stream applicants.',
    f'{BASE_URL}/alberta-crs-calculator.html',
    'alberta crs score calculator, crs calculator alberta, alberta pnp crs score calculator, crs score calculator for alberta',
    '''
    <h2>Alberta Immigrant Nominee Program (AINP)</h2>
    <p>The Alberta Immigrant Nominee Program (AINP) is Alberta's provincial immigration program that allows the province to nominate immigrants who will contribute to Alberta's growing economy. Alberta is one of Canada's fastest-growing provinces, with a booming energy sector, technology industry, and diversified economy that creates strong demand for skilled workers.</p>

    <h2>AINP Express Entry Stream</h2>
    <p>The AINP Express Entry Stream is Alberta's main pathway for candidates already in the federal Express Entry pool. Alberta reviews Express Entry profiles and issues Notifications of Interest (NOIs) to candidates who best match Alberta's labour market needs. The AINP Express Entry Stream targets three sub-categories:</p>
    <ul>
      <li><strong>Alberta Express Entry Stream:</strong> For candidates in the Express Entry pool with skills aligned with Alberta's economic priorities</li>
      <li><strong>Self-Employed Farmer Stream:</strong> For experienced farmers intending to purchase and operate a farm in Alberta</li>
      <li><strong>Rural Renewal Stream:</strong> For candidates with job offers in designated rural Alberta communities</li>
    </ul>

    <h2>Alberta Opportunity Stream (AOS)</h2>
    <p>The Alberta Opportunity Stream (AOS) is for temporary foreign workers and international students already living and working in Alberta. It operates outside Express Entry but can still lead to permanent residence through a base PNP nomination. AOS requires a valid job offer, language proficiency, and minimum education requirements.</p>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">600</div><div class="stat-label">CRS Points After AINP Nomination</div></div>
      <div class="stat-card"><div class="stat-value">#4</div><div class="stat-label">Alberta Largest Canadian Province</div></div>
      <div class="stat-card"><div class="stat-value">0%</div><div class="stat-label">Provincial Income Tax (some years)</div></div>
      <div class="stat-card"><div class="stat-value">~480</div><div class="stat-label">Typical Base CRS for AINP NOI</div></div>
    </div>
    ''',
    '''
    <h2>Alberta CRS Score Requirements</h2>
    <p>AINP does not publish a fixed minimum CRS score for the Express Entry Stream. Instead, Alberta reviews Express Entry pool profiles periodically and issues NOIs based on current labour market needs and available provincial nomination allocation. Candidates with higher CRS scores and in-demand occupations are more likely to receive an NOI.</p>

    <h2>In-Demand Occupations in Alberta</h2>
    <p>Alberta's economy is primarily driven by the energy sector (oil and gas), agriculture, construction, and a growing tech sector in Calgary. In-demand occupations include engineers (especially petroleum engineers), IT professionals, healthcare workers, financial services workers, and tradespeople. Having experience in these sectors significantly improves your chances of receiving an AINP NOI.</p>

    <h2>How to Apply for AINP</h2>
    <p>For the Express Entry Stream: (1) Create an Express Entry profile and enter the pool; (2) Wait for an NOI from Alberta or check for self-selection opportunities; (3) Accept the NOI and complete the AINP application; (4) Upon nomination, receive 600 CRS points automatically; (5) Receive ITA in the next Express Entry draw. Use our <a href="/pnp-crs-calculator.html">PNP CRS Calculator</a> to see your score with the +600 nomination bonus. You can also compare with <a href="/ontario-crs-calculator.html">Ontario's OINP</a> to find the best provincial fit for your profile.</p>
    ''',
    [
        ("What is the minimum CRS score for the AINP Express Entry stream?", "AINP does not publish a fixed minimum CRS score. Alberta reviews Express Entry profiles and issues NOIs based on labour market needs. Generally, candidates with CRS scores of 400+ and in-demand occupations have better chances of receiving an AINP NOI."),
        ("How does Alberta's AINP nomination affect my Express Entry CRS score?", "Receiving an AINP nomination through the Express Entry-linked stream adds 600 points to your CRS score, effectively putting you at 1,000+ total, which is well above any historical Express Entry draw cutoff."),
        ("What occupations does Alberta prioritize for AINP?", "Alberta prioritizes occupations in its key economic sectors: oil and gas (engineers, technologists), construction, healthcare, technology, agriculture, and business/financial services. Having an Alberta job offer in one of these sectors strengthens your AINP application."),
        ("Can I apply for AINP without a job offer?", "Yes. The AINP Express Entry Stream does not require a job offer — Alberta may issue an NOI based on your Express Entry profile alone. However, having a job offer from an Alberta employer can strengthen your application and may be required for the Alberta Opportunity Stream."),
        ("How long does AINP processing take?", "AINP processing times vary but are typically 3–6 months for the Express Entry Stream after submitting a completed application. Total timeline from NOI to permanent residence (including Express Entry processing) is approximately 12–18 months.")
    ],
    [("Official Alberta Immigrant Nominee Program", "https://www.alberta.ca/alberta-immigrant-nominee-program"),
     ("IRCC Express Entry", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html")]
)


make_calculator_page(
    'ontario-crs-calculator.html',
    'Ontario CRS Calculator – OINP Express Entry Stream Points Tool',
    'Ontario CRS Calculator – OINP Express Entry Human Capital Priorities',
    'Calculate your CRS score for Ontario\'s PNP (OINP). Free Ontario CRS calculator for the Human Capital Priorities and Express Entry streams.',
    f'{BASE_URL}/ontario-crs-calculator.html',
    'crs score calculator ontario, crs calculator ontario, crs score calculator for ontario, crs score calculator for ontario pnp',
    '''
    <h2>Ontario Immigrant Nominee Program (OINP)</h2>
    <p>The Ontario Immigrant Nominee Program (OINP) is Canada's largest and most competitive provincial nominee program. Ontario, as Canada's most populous province and economic hub, receives the highest number of immigration nominations annually. The OINP has several streams designed to attract skilled workers, international graduates, and entrepreneurs who wish to settle and work in Ontario.</p>

    <h2>OINP Express Entry-Aligned Streams</h2>
    <p>Ontario has three main Express Entry-aligned streams:</p>
    <ul>
      <li><strong>Human Capital Priorities Stream:</strong> Targets candidates in the Express Entry pool with post-secondary education and high language scores. Ontario sends NOIs to qualifying profiles based on their CRS score and occupation.</li>
      <li><strong>Skilled Trades Stream:</strong> For candidates in Express Entry with work experience in specific skilled trades (NOC TEER 2) and a job offer from an Ontario employer.</li>
      <li><strong>French-Speaking Skilled Worker Stream:</strong> For francophone candidates in the Express Entry pool who have CLB 7+ in French and meet the language requirements.</li>
    </ul>

    <h2>OINP Human Capital Priorities</h2>
    <p>The Human Capital Priorities (HCP) Stream is the most active OINP Express Entry stream. Ontario conducts periodic draws from the Express Entry pool, sending NOIs to candidates who have specific occupations and meet minimum CRS scores. The HCP stream does not require a job offer, making it particularly attractive for candidates with strong profiles but no Canadian employer connection.</p>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">#1</div><div class="stat-label">Province by Nomination Volume</div></div>
      <div class="stat-card"><div class="stat-value">600</div><div class="stat-label">CRS Points After OINP Nomination</div></div>
      <div class="stat-card"><div class="stat-value">CLB 7</div><div class="stat-label">Typical Language Minimum for HCP</div></div>
      <div class="stat-card"><div class="stat-value">~400+</div><div class="stat-label">Typical Base CRS for HCP NOIs</div></div>
    </div>
    ''',
    '''
    <h2>Ontario Employer Job Offer and OINP</h2>
    <p>While the HCP Stream does not require a job offer, having an Ontario employer job offer can make you eligible for the Employer Job Offer Streams, which have different (often lower) CRS requirements. An Ontario job offer combined with a nomination can dramatically accelerate your pathway to Canadian PR.</p>

    <h2>Toronto vs Rest of Ontario</h2>
    <p>Toronto, Ottawa, and Hamilton-Niagara are Ontario's major immigration destinations. Many OINP streams require or prefer candidates who will settle in Ontario (outside Toronto for some streams). Ontario's technology sector (particularly in the Toronto-Waterloo corridor), financial services, healthcare, and manufacturing sectors are the primary drivers of immigration demand.</p>

    <h2>How to Apply for OINP</h2>
    <p>For Express Entry-aligned streams: (1) Create an active Express Entry profile; (2) Register your interest with the OINP through their online portal; (3) Wait for an NOI or respond to an Express Entry Draw; (4) Accept the NOI and complete the OINP application within the deadline; (5) Receive the nomination and +600 CRS points. Compare with <a href="/bc-crs-calculator.html">BC PNP</a> or <a href="/alberta-crs-calculator.html">Alberta AINP</a> to find the best provincial option for your profile.</p>
    ''',
    [
        ("What is the minimum CRS score for OINP Human Capital Priorities?", "OINP does not publish a fixed minimum CRS score. Cutoffs vary by draw. The HCP stream typically targets candidates with CRS scores of 400 or above who work in priority occupations. Some tech-specific draws have had lower cutoffs around 350–400."),
        ("Does Ontario have a tech-specific immigration stream?", "Yes, Ontario's OINP has conducted targeted draws for tech workers within the Human Capital Priorities stream, with specific NOC codes in information technology, engineering, and science sectors. Check the OINP website for current draws."),
        ("Can I apply for OINP without a job offer?", "Yes. The Human Capital Priorities Stream does not require a job offer. However, the Employer Job Offer International Student and Foreign Worker streams do require an Ontario employer job offer."),
        ("How does OINP nomination affect my CRS score?", "An OINP nomination through the Express Entry-aligned stream adds exactly 600 CRS points to your profile. This puts your total CRS score well above all historical Express Entry draw cutoffs, virtually guaranteeing an ITA."),
        ("How long does OINP processing take?", "OINP processing times for the Express Entry streams are typically 30–90 days after submitting a complete application following an NOI. Once nominated, IRCC will add the 600 points and you'll receive an ITA in the next available draw.")
    ],
    [("Official OINP Website", "https://www.ontario.ca/page/ontario-immigrant-nominee-program-oinp"),
     ("IRCC Express Entry", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html")]
)


make_calculator_page(
    'bc-crs-calculator.html',
    'BC CRS Calculator – British Columbia PNP Express Entry Points Tool',
    'British Columbia CRS Calculator – BC PNP Express Entry Stream',
    'Calculate your CRS score for British Columbia\'s Provincial Nominee Program (BC PNP). Free BC CRS calculator for Express Entry applicants.',
    f'{BASE_URL}/bc-crs-calculator.html',
    'crs calculator bc, crs score calculator bc, crs score calculator for bc pnp, bc pnp crs calculator',
    '''
    <h2>British Columbia Provincial Nominee Program (BC PNP)</h2>
    <p>The British Columbia Provincial Nominee Program (BC PNP) is one of Canada's most popular and competitive provincial immigration programs. British Columbia, known for its stunning natural beauty, mild climate, and thriving technology sector, attracts tens of thousands of skilled immigrants annually. The BC PNP has multiple streams for skilled workers, international graduates, and entrepreneurs.</p>

    <h2>BC PNP Express Entry BC (EEBC) Streams</h2>
    <p>The Express Entry BC (EEBC) streams are BC PNP's Express Entry-linked immigration pathways:</p>
    <ul>
      <li><strong>Skilled Worker in BC:</strong> For candidates with a job offer from a BC employer in a NOC TEER 0, 1, 2, or 3 occupation and 2+ years of relevant work experience</li>
      <li><strong>Healthcare Professional:</strong> For internationally trained healthcare workers with a BC job offer</li>
      <li><strong>International Graduate:</strong> For recent graduates from eligible Canadian post-secondary institutions with a BC job offer</li>
      <li><strong>Entry Level and Semi-Skilled Worker:</strong> For workers in tourism, food services, long-haul trucking, or Northeast BC industries</li>
    </ul>

    <h2>BC Tech Pilot Program</h2>
    <p>British Columbia actively recruits technology workers through targeted streams within BC PNP. Tech occupations in BC (particularly Vancouver and Victoria) are in extremely high demand. The province regularly conducts tech draws with lower score thresholds to attract IT professionals.</p>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">600</div><div class="stat-label">CRS Points After BC PNP Nomination</div></div>
      <div class="stat-card"><div class="stat-value">#3</div><div class="stat-label">BC Population Ranking in Canada</div></div>
      <div class="stat-card"><div class="stat-value">100+</div><div class="stat-label">BC PNP Draws Per Year</div></div>
      <div class="stat-card"><div class="stat-value">TEER 0-3</div><div class="stat-label">Eligible NOC Categories</div></div>
    </div>
    ''',
    '''
    <h2>BC PNP Registration Score System</h2>
    <p>BC PNP uses its own BC PNP score system (separate from CRS) to rank candidates and issue invitations to apply. The BC PNP score is based on factors including job offer details, regional district, NOC code, and your Express Entry CRS score. Candidates with high BC PNP scores in their target category are invited to apply for provincial nomination.</p>

    <h2>Vancouver and the Tech Corridor</h2>
    <p>Vancouver consistently ranks among the world's most livable cities and has one of North America's fastest-growing technology ecosystems. The city is home to major tech companies including Amazon, Microsoft, Apple, EA Games, and hundreds of startups. For tech workers, BC PNP's tech pathway can be one of the fastest routes to Canadian permanent residence.</p>

    <h2>How to Apply for BC PNP</h2>
    <p>For the EEBC streams: (1) Ensure you have an active Express Entry profile; (2) Register on the BC PNP Online portal; (3) Receive an invitation to apply from BC based on your BC PNP score; (4) Complete the BC PNP application within the deadline; (5) Receive the nomination and +600 CRS points. Compare options with <a href="/alberta-crs-calculator.html">Alberta AINP</a> or our <a href="/pnp-crs-calculator.html">main PNP Calculator</a>.</p>
    ''',
    [
        ("Does BC PNP require a job offer?", "Most BC PNP streams require a valid BC employer job offer in a qualifying NOC occupation. However, the requirements vary by stream — some streams may have exceptions for candidates in specific sectors or circumstances."),
        ("What is the minimum score for BC PNP?", "BC PNP uses its own scoring system separate from CRS. Minimum BC PNP scores vary by stream and change with each draw. Tech streams may have lower thresholds. Check the BC PNP website for current minimum scores by stream."),
        ("Can international students apply for BC PNP?", "Yes. The BC PNP International Graduate category targets recent graduates from eligible Canadian post-secondary institutions who have a BC job offer. This is an excellent pathway for international students who have studied in BC."),
        ("How long does BC PNP processing take?", "After receiving an invitation and submitting a complete application, BC PNP typically processes applications within 2–3 months. Once nominated, receiving an ITA through Express Entry can happen in the next draw, and IRCC PR processing takes approximately 6–12 months."),
        ("Is BC a good province for tech workers to immigrate to?", "Yes. British Columbia, particularly the Greater Vancouver and Victoria areas, is one of the top destinations for tech workers globally. The BC PNP tech streams are designed to fast-track tech professionals, and Vancouver's tech ecosystem offers strong career opportunities.")
    ],
    [("Official BC PNP Website", "https://www.welcomebc.ca/immigrate-to-b-c/bc-provincial-nominee-program"),
     ("IRCC Express Entry", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html")]
)


make_calculator_page(
    'manitoba-crs-calculator.html',
    'Manitoba CRS Calculator – MPNP Express Entry Stream Points Tool',
    'Manitoba CRS Calculator – MPNP Express Entry Pathway',
    'Calculate your CRS score for the Manitoba Provincial Nominee Program (MPNP). Free Manitoba CRS calculator for Express Entry stream applicants.',
    f'{BASE_URL}/manitoba-crs-calculator.html',
    'crs score calculator manitoba, crs score calculator for manitoba, crs score calculator for manitoba pnp, calculate crs score for manitoba pnp',
    '''
    <h2>Manitoba Provincial Nominee Program (MPNP)</h2>
    <p>The Manitoba Provincial Nominee Program (MPNP) is one of Canada's more accessible provincial immigration programs, particularly for skilled workers who have connections to Manitoba through family ties, previous work experience, or employer job offers. Manitoba actively recruits immigrants to address significant labour shortages in key sectors including healthcare, agriculture, manufacturing, and transportation.</p>

    <h2>MPNP Skilled Worker Streams</h2>
    <p>The MPNP has two main skilled worker pathways:</p>
    <ul>
      <li><strong>Skilled Workers in Manitoba (SWM):</strong> For foreign workers currently working in Manitoba with a permanent full-time job offer from a Manitoba employer and at least 6 months of Manitoba work experience</li>
      <li><strong>Skilled Workers Overseas (SWO):</strong> For workers outside Canada who have either a Manitoba job offer OR a connection to Manitoba through family members who are Canadian citizens or PRs residing in Manitoba</li>
      <li><strong>International Education Stream:</strong> For international graduates from Manitoba post-secondary institutions who have a Manitoba job offer</li>
    </ul>

    <h2>MPNP and Express Entry</h2>
    <p>The MPNP operates in conjunction with Express Entry. Candidates in the Express Entry pool may receive a Letter of Advice to Apply (LAA) from Manitoba, and successful nominees receive 600 additional CRS points. Manitoba conducts regular MPNP draws and frequently targets specific occupations in healthcare, engineering, and construction.</p>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">600</div><div class="stat-label">CRS Points After MPNP Nomination</div></div>
      <div class="stat-card"><div class="stat-value">Lower</div><div class="stat-label">Cost of Living vs Toronto/Vancouver</div></div>
      <div class="stat-card"><div class="stat-value">French</div><div class="stat-label">Bilingual Province (Manitoba)</div></div>
      <div class="stat-card"><div class="stat-value">~300+</div><div class="stat-label">Typical Base CRS for MPNP Draws</div></div>
    </div>
    ''',
    '''
    <h2>Manitoba's Strategic Immigration Goals</h2>
    <p>Manitoba uses immigration strategically to address its labour market challenges. The province prioritizes candidates with experience in healthcare (physicians, nurses, allied health), agriculture and agribusiness, manufacturing, construction trades, and information technology. Having experience in these fields or a Manitoba connection significantly improves your chances of receiving an MPNP LAA.</p>

    <h2>Living in Manitoba</h2>
    <p>Winnipeg, Manitoba's capital, is a diverse and growing city with a significantly lower cost of living compared to Toronto or Vancouver. Manitoba offers excellent public services, strong Indigenous cultural heritage, and growing career opportunities. The province has a rapidly expanding tech sector and is home to some of Canada's largest Indigenous business enterprises.</p>

    <h2>How to Apply for MPNP</h2>
    <p>For Express Entry-linked MPNP: (1) Create an Express Entry profile; (2) Register interest on the MPNP portal and indicate connections to Manitoba; (3) Receive a Letter of Advice to Apply from Manitoba; (4) Complete the MPNP application within the deadline; (5) Receive the nomination and +600 CRS points. Compare with <a href="/saskatchewan-crs-calculator.html">Saskatchewan SINP</a> for nearby prairie province options.</p>
    ''',
    [
        ("What is the minimum CRS score for MPNP?", "MPNP does not have a fixed minimum CRS score. However, candidates in the Express Entry pool typically need a minimum CRS score to be invited. Prairie province programs like MPNP often have lower effective cutoffs than BC or Ontario, making them accessible for candidates with mid-range scores."),
        ("Do I need a Manitoba connection for MPNP?", "A Manitoba connection (Manitoba job offer, family in Manitoba, or previous Manitoba work/study experience) significantly strengthens an MPNP application. The Skilled Workers Overseas stream specifically requires either a Manitoba job offer or a Manitoba connection through family."),
        ("What sectors does Manitoba target for immigration?", "Manitoba prioritizes healthcare workers (especially nurses and physicians for rural areas), skilled trades, agriculture/agribusiness, manufacturing, transportation, and information technology. These are the sectors with the most critical labour shortages in the province."),
        ("Can international students apply for MPNP?", "Yes. The MPNP International Education Stream allows graduates from eligible Manitoba post-secondary institutions to apply for provincial nomination if they have a Manitoba employer job offer after graduation."),
        ("What is life like for immigrants in Manitoba?", "Winnipeg has a strong and welcoming immigrant community, particularly from the Philippines, India, and Ukraine. The cost of living is significantly lower than in Toronto or Vancouver. Manitoba offers good public services, excellent schools, and growing economic opportunities.")
    ],
    [("Official MPNP Website", "https://immigratemanitoba.com/immigrate-to-manitoba/mpnp/"),
     ("IRCC Express Entry", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html")]
)


make_calculator_page(
    'saskatchewan-crs-calculator.html',
    'Saskatchewan CRS Calculator – SINP Express Entry Points Tool',
    'Saskatchewan CRS Calculator – SINP Express Entry Category',
    'Calculate your CRS score for the Saskatchewan Immigrant Nominee Program (SINP). Free Saskatchewan CRS calculator for Express Entry applicants.',
    f'{BASE_URL}/saskatchewan-crs-calculator.html',
    'crs score calculator saskatchewan, saskatchewan crs calculator',
    '''
    <h2>Saskatchewan Immigrant Nominee Program (SINP)</h2>
    <p>The Saskatchewan Immigrant Nominee Program (SINP) is Saskatchewan's provincial immigration program designed to attract skilled workers, entrepreneurs, and farmers to support the province's growing economy. Saskatchewan, with its agricultural powerhouse, mining industry, and growing technology sector, offers strong immigration opportunities for a diverse range of skilled professionals.</p>

    <h2>SINP International Skilled Worker Category</h2>
    <p>The SINP International Skilled Worker (ISW) category has two streams:</p>
    <ul>
      <li><strong>Saskatchewan Express Entry:</strong> For candidates in the Express Entry pool who score high on SINP's points assessment and meet Saskatchewan's occupational needs. This stream uses the Saskatchewan Points Assessment to rank candidates.</li>
      <li><strong>Occupations In-Demand:</strong> For workers in occupations on Saskatchewan's In-Demand Occupations List, with a minimum of one year of work experience in the target occupation in the past 10 years.</li>
    </ul>

    <h2>SINP Saskatchewan Experience Category</h2>
    <p>The Saskatchewan Experience Category has multiple streams for workers already employed in Saskatchewan. It includes the Existing Work Permit, Health Professionals, and Students streams. These pathways are especially valuable for temporary foreign workers who have established themselves in Saskatchewan.</p>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">600</div><div class="stat-label">CRS Points After SINP Nomination</div></div>
      <div class="stat-card"><div class="stat-value">60%</div><div class="stat-label">Canada's Agricultural Output from Prairies</div></div>
      <div class="stat-card"><div class="stat-value">Low</div><div class="stat-label">Cost of Living vs Major Cities</div></div>
      <div class="stat-card"><div class="stat-value">~300+</div><div class="stat-label">Typical Base CRS for SINP</div></div>
    </div>
    ''',
    '''
    <h2>Saskatchewan's In-Demand Occupations</h2>
    <p>Saskatchewan regularly updates its In-Demand Occupations List based on labour market data. High-priority sectors include: agriculture and agri-food, energy and resources (oil and mining), healthcare (physicians, nurses, and allied health professionals), construction and trades, and information technology. Checking the current SINP In-Demand Occupations List is an important first step for potential applicants.</p>

    <h2>Living and Working in Saskatchewan</h2>
    <p>Saskatoon and Regina are Saskatchewan's two main cities, both offering affordable housing, good public services, and growing career opportunities. Saskatchewan's economy is diversified across agriculture, mining, oil, and manufacturing, providing stable employment across multiple sectors. The province is known for its friendly communities and high quality of life.</p>

    <h2>How to Apply for SINP</h2>
    <p>For SINP Saskatchewan Express Entry: (1) Have an active Express Entry profile and meet basic Express Entry eligibility; (2) Create a SINP profile and complete the Saskatchewan Points Assessment; (3) Wait for SINP draws when higher-scoring candidates are issued invitations to apply; (4) Complete the SINP application; (5) Receive the nomination and +600 CRS points. Compare your options with <a href="/manitoba-crs-calculator.html">Manitoba MPNP</a> or use our main <a href="/pnp-crs-calculator.html">PNP CRS Calculator</a>.</p>
    ''',
    [
        ("What is the SINP points assessment?", "SINP uses its own points assessment system for the International Skilled Worker category. Points are awarded for education, work experience, language ability, age, Saskatchewan connections, and adaptability factors. Candidates with the highest SINP points are invited to apply when SINP draws occur."),
        ("Do I need a job offer for SINP?", "A job offer from a Saskatchewan employer is not required for all SINP streams. The Occupations In-Demand stream does not require a job offer. However, having a Saskatchewan employer job offer strengthens your application significantly."),
        ("What occupations does Saskatchewan prioritize?", "Saskatchewan prioritizes agriculture and agri-food workers, healthcare professionals (especially for rural areas), oil/gas and mining workers, construction trades, and technology workers. Check the current SINP In-Demand Occupations List for specific NOC codes."),
        ("Can I apply for SINP while living outside Canada?", "Yes. The International Skilled Worker – Saskatchewan Express Entry and Occupations In-Demand streams are open to candidates living abroad. You do not need to be in Saskatchewan or Canada to apply."),
        ("How does SINP nomination connect to Express Entry?", "If you have an active Express Entry profile and receive an SINP nomination through the Saskatchewan Express Entry stream, IRCC will add 600 CRS points to your profile. You will then receive an ITA in the next Express Entry draw.")
    ],
    [("Official SINP Website", "https://www.saskatchewan.ca/residents/moving-to-saskatchewan/immigrating-to-saskatchewan"),
     ("IRCC Express Entry", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html")]
)


make_calculator_page(
    'nova-scotia-crs-calculator.html',
    'Nova Scotia CRS Calculator – NSNP Express Entry Stream Points Tool',
    'Nova Scotia CRS Calculator – NSNP Express Entry Stream',
    'Calculate your CRS score for the Nova Scotia Nominee Program (NSNP). Free Nova Scotia CRS calculator for Express Entry applicants targeting the Atlantic provinces.',
    f'{BASE_URL}/nova-scotia-crs-calculator.html',
    'crs score calculator for nova scotia, how to calculate crs score for nova scotia',
    '''
    <h2>Nova Scotia Nominee Program (NSNP)</h2>
    <p>The Nova Scotia Nominee Program (NSNP) is Nova Scotia's provincial immigration pathway that nominates skilled workers, entrepreneurs, and international graduates who will contribute to Nova Scotia's economy. Nova Scotia, located on Canada's Atlantic coast, offers a unique immigration experience with stunning coastal landscapes, affordable living, and growing career opportunities in key sectors.</p>

    <h2>NSNP Express Entry Streams</h2>
    <p>Nova Scotia has several Express Entry-aligned immigration streams:</p>
    <ul>
      <li><strong>Nova Scotia Labour Market Priorities Stream:</strong> Allows Nova Scotia to search the Express Entry pool directly and issue NOIs to candidates with specific skills needed in the province's labour market. This is the main Express Entry-linked stream.</li>
      <li><strong>Nova Scotia Demand: Express Entry Stream:</strong> For candidates who have received an official job offer from a Nova Scotia employer and meet experience requirements.</li>
      <li><strong>Nova Scotia Healthcare Stream:</strong> A dedicated stream for healthcare professionals, particularly nurses and physicians, addressing critical shortages in the province.</li>
    </ul>

    <h2>Atlantic Immigration Program (AIP)</h2>
    <p>Nova Scotia also participates in the Atlantic Immigration Program (AIP), a federal-provincial initiative designed to attract and retain skilled workers in the Atlantic provinces. AIP requires a designated employer job offer and is separate from but complementary to the NSNP streams.</p>

    <div class="stat-grid">
      <div class="stat-card"><div class="stat-value">600</div><div class="stat-label">CRS Points After NSNP Nomination</div></div>
      <div class="stat-card"><div class="stat-value">AIP</div><div class="stat-label">Atlantic Immigration Program Partner</div></div>
      <div class="stat-card"><div class="stat-value">Low</div><div class="stat-label">Cost of Living vs National Average</div></div>
      <div class="stat-card"><div class="stat-value">Oceans</div><div class="stat-label">Technology & Fisheries Economy</div></div>
    </div>
    ''',
    '''
    <h2>Nova Scotia's Priority Sectors for Immigration</h2>
    <p>Nova Scotia focuses its immigration programs on sectors with critical labour market needs including: healthcare (nurses, physicians, allied health professionals), technology and oceans technology, construction and skilled trades, agriculture and agri-food, and financial services. Halifax, the provincial capital, has a growing technology and startup ecosystem.</p>

    <h2>Living in Nova Scotia</h2>
    <p>Halifax is a vibrant, diverse city with world-class universities (Dalhousie University, Saint Mary's University), excellent quality of life, and housing costs significantly below Toronto and Vancouver. Nova Scotia's combination of natural beauty, cultural richness, and economic opportunity makes it an increasingly popular choice for skilled immigrants.</p>

    <h2>How to Maximize Your Chances with NSNP</h2>
    <p>To improve your chances with the NSNP: (1) Have an active Express Entry profile with strong core CRS factors; (2) Consider obtaining a Nova Scotia job offer through the province's job portal or employer networks; (3) Healthcare professionals should apply directly to the NSNP Healthcare Stream; (4) Research the current NSNP Labour Market Priorities to ensure your occupation is in demand. Also compare opportunities with the <a href="/pnp-crs-calculator.html">PNP CRS Calculator</a> and consider whether another province like <a href="/ontario-crs-calculator.html">Ontario</a> or <a href="/bc-crs-calculator.html">BC</a> might be a better fit.</p>
    ''',
    [
        ("Does Nova Scotia have a healthcare immigration stream?", "Yes. Nova Scotia has a dedicated healthcare stream for in-demand healthcare occupations, particularly registered nurses and physicians. This stream addresses critical healthcare shortages in the province and often has more accessible requirements than general streams."),
        ("What is the Atlantic Immigration Program (AIP)?", "The Atlantic Immigration Program (AIP) is a federal program that allows designated employers in Atlantic Canada (Nova Scotia, New Brunswick, PEI, Newfoundland) to hire foreign workers for full-time positions that cannot be filled locally. AIP-designated employers can sponsor foreign workers for permanent residence."),
        ("What is the cost of living in Nova Scotia?", "Nova Scotia has one of the lowest costs of living among Canada's provinces with significant cities. Halifax's housing costs are significantly lower than Toronto, Vancouver, or Calgary, making it attractive for immigrants seeking affordable quality of life."),
        ("Can I get a Nova Scotia nomination with a low CRS score?", "Yes. The NSNP Labour Market Priorities stream allows Nova Scotia to target candidates based on labour market needs, not just CRS score. Candidates with specific in-demand skills may receive an NOI even with a relatively lower base CRS score. Once nominated, the 600 CRS points added will guarantee an ITA."),
        ("How does the NSNP nomination process work?", "For Express Entry-linked NSNP streams, Nova Scotia searches the Express Entry pool and issues NOIs to qualifying candidates. After accepting the NOI, candidates complete the provincial application. Once approved, the 600-point nomination is added to the candidate's Express Entry profile.")
    ],
    [("Official Nova Scotia Immigration", "https://novascotiaimmigration.com/"),
     ("IRCC Express Entry", "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html")]
)

print("Provincial pages created")
