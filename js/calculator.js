/**
 * CRS Score Calculator - Full IRCC CRS Grid Logic
 * Based on official IRCC Comprehensive Ranking System
 * Site: crsscorecalculator.vercel.app
 */

'use strict';

// =========================================================
// IRCC CRS POINTS TABLES (Official Values)
// =========================================================

const CRS = {

  // --- SECTION A: Age Points ---
  // [withSpouse, withoutSpouse]
  age: {
    'under18':  [0, 0],
    '18':       [90, 99],
    '19':       [95, 105],
    '20':       [100, 110],
    '21':       [100, 110],
    '22':       [100, 110],
    '23':       [100, 110],
    '24':       [100, 110],
    '25':       [100, 110],
    '26':       [100, 110],
    '27':       [100, 110],
    '28':       [100, 110],
    '29':       [100, 110],
    '30':       [95, 105],
    '31':       [90, 99],
    '32':       [85, 94],
    '33':       [80, 88],
    '34':       [75, 83],
    '35':       [70, 77],
    '36':       [65, 72],
    '37':       [60, 66],
    '38':       [55, 61],
    '39':       [50, 55],
    '40':       [45, 50],
    '41':       [35, 39],
    '42':       [25, 28],
    '43':       [15, 17],
    '44':       [5, 6],
    '45plus':   [0, 0]
  },

  // --- SECTION A: Education Points ---
  // [withSpouse, withoutSpouse]
  education: {
    'none':       [0, 0],
    'secondary':  [28, 30],
    'one_year':   [84, 90],
    'two_year':   [91, 98],
    'bachelors':  [112, 120],
    'two_or_more':[119, 128],
    'masters':    [126, 135],
    'phd':        [140, 150]
  },

  // --- SECTION A: First Language CLB → Points ---
  // Single applicant: Speaking/Listening/Reading/Writing each scored separately
  // CLB levels 4–10 (CLB 10+ treated as 10)
  language1_single: {
    speaking:  { 4:6,  5:6,  6:8,  7:16, 8:22, 9:29, 10:32 },
    listening: { 4:6,  5:6,  6:8,  7:16, 8:22, 9:29, 10:32 },
    reading:   { 4:6,  5:6,  6:8,  7:16, 8:22, 9:29, 10:32 },
    writing:   { 4:6,  5:6,  6:8,  7:16, 8:22, 9:29, 10:32 }
  },
  // With spouse (different point grid)
  language1_spouse: {
    speaking:  { 4:6,  5:6,  6:8,  7:16, 8:22, 9:29, 10:32 },
    listening: { 4:6,  5:6,  6:8,  7:16, 8:22, 9:29, 10:32 },
    reading:   { 4:6,  5:6,  6:8,  7:16, 8:22, 9:29, 10:32 },
    writing:   { 4:6,  5:6,  6:8,  7:16, 8:22, 9:29, 10:32 }
  },

  // --- SECTION A: Second Official Language ---
  language2: {
    // Max 22 pts: each skill 4 pts for CLB 5-8, then 6 pts for CLB 9+
    // But only if CLB 5+ in all 4 abilities; 4 pts each ability CLB 5-8, 6 pts CLB 9+
    skills: { 4:0, 5:1, 6:1, 7:3, 8:3, 9:6, 10:6 }
    // Max 22 pts total for second language
  },

  // --- SECTION A: Canadian Work Experience ---
  // [withSpouse, withoutSpouse]
  canadianWE: {
    '0':   [0, 0],
    '1':   [35, 40],
    '2':   [46, 53],
    '3':   [56, 64],
    '4':   [63, 72],
    '5':   [70, 80]
  },

  // --- SECTION B: Spouse/Partner Factors ---
  spouse_education: {
    'none':       2,
    'secondary':  2,
    'one_year':   7,
    'two_year':   8,
    'bachelors':  10,
    'two_or_more': 10,
    'masters':    10,
    'phd':        10
  },
  spouse_language: {
    // Spouse CLB → points per skill (max 20 pts total: 5 pts each ability)
    skills: { 4:0, 5:1, 6:1, 7:3, 8:3, 9:5, 10:5 }
    // Max 20 pts
  },
  spouse_canadianWE: {
    '0': 0,
    '1': 5,
    '2': 7,
    '3': 8,
    '4': 9,
    '5': 10
  },

  // --- SECTION C: Skill Transferability ---
  // Education + Language
  // With post-secondary credential + CLB 7+
  skillTransfer: {
    // Education + CLB 7-8 = 13, CLB 9+ = 25; max 50 total with foreign WE
    // Education with foreign WE: 1-2 yrs = 13, 3+ yrs = 25; max 50
    // Foreign WE + CLB 7-8 = 13, CLB 9+ = 25; max 50
    // Trade Cert + CLB 5-6 = 13, CLB 7+ = 25; max 50
    educationLang: {
      clb7_8: 13,
      clb9plus: 25
    },
    educationFWE: {
      one_two_yr: 13,
      three_plus_yr: 25
    },
    foreignWELang: {
      clb7_8: 13,
      clb9plus: 25
    },
    tradesCert: {
      clb5_6: 13,
      clb7plus: 25
    }
  },

  // --- SECTION D: Additional Points ---
  additional: {
    pnp: 600,
    jobOffer_00: 200,       // NOC TEER 0 Major Group 00
    jobOffer_other: 50,     // NOC TEER 0,1,2,3 other
    sibling: 15,
    french_strong: 50,      // French CLB 7+ with English CLB 5+
    french_weak: 25,        // French CLB 7+ with English CLB 4 or less
    canadian_edu_1_2: 15,   // 1–2 year post-secondary
    canadian_edu_3plus: 30  // 3+ year post-secondary
  }
};

// =========================================================
// CLB CONVERSION TABLES (Test Score → CLB)
// =========================================================

const CLB_CONVERSION = {

  IELTS: {
    speaking: [
      { min: 0,   max: 3.9,  clb: 3 },
      { min: 4.0, max: 4.9,  clb: 4 },
      { min: 5.0, max: 5.9,  clb: 5 },
      { min: 6.0, max: 6.9,  clb: 6 },
      { min: 7.0, max: 7.4,  clb: 7 },
      { min: 7.5, max: 8.4,  clb: 8 },
      { min: 8.5, max: 9.0,  clb: 9 }
    ],
    listening: [
      { min: 0,   max: 3.4,  clb: 3 },
      { min: 3.5, max: 3.9,  clb: 4 },
      { min: 4.0, max: 4.4,  clb: 5 },
      { min: 4.5, max: 4.9,  clb: 6 },
      { min: 5.0, max: 5.9,  clb: 7 },
      { min: 6.0, max: 7.4,  clb: 8 },
      { min: 7.5, max: 8.4,  clb: 9 },
      { min: 8.5, max: 9.0,  clb: 10 }
    ],
    reading: [
      { min: 0,   max: 2.9,  clb: 3 },
      { min: 3.0, max: 3.4,  clb: 4 },
      { min: 3.5, max: 3.9,  clb: 5 },
      { min: 4.0, max: 4.9,  clb: 6 },
      { min: 5.0, max: 5.9,  clb: 7 },
      { min: 6.0, max: 6.9,  clb: 8 },
      { min: 7.0, max: 7.9,  clb: 9 },
      { min: 8.0, max: 9.0,  clb: 10 }
    ],
    writing: [
      { min: 0,   max: 3.9,  clb: 3 },
      { min: 4.0, max: 4.9,  clb: 4 },
      { min: 5.0, max: 5.4,  clb: 5 },
      { min: 5.5, max: 5.9,  clb: 6 },
      { min: 6.0, max: 6.4,  clb: 7 },
      { min: 6.5, max: 7.4,  clb: 8 },
      { min: 7.5, max: 8.4,  clb: 9 },
      { min: 8.5, max: 9.0,  clb: 10 }
    ]
  },

  CELPIP: {
    // CELPIP score directly maps to CLB
    speaking:  { 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:10, 12:10 },
    listening: { 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:10, 12:10 },
    reading:   { 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:10, 12:10 },
    writing:   { 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:10, 12:10 }
  },

  TEF: {
    // TEF Canada expression orale (speaking) → CLB
    speaking: [
      { min: 0,   max: 180, clb: 3 },
      { min: 181, max: 225, clb: 4 },
      { min: 226, max: 270, clb: 5 },
      { min: 271, max: 309, clb: 6 },
      { min: 310, max: 348, clb: 7 },
      { min: 349, max: 370, clb: 8 },
      { min: 371, max: 393, clb: 9 },
      { min: 394, max: 450, clb: 10 }
    ],
    listening: [
      { min: 0,   max: 144, clb: 3 },
      { min: 145, max: 180, clb: 4 },
      { min: 181, max: 216, clb: 5 },
      { min: 217, max: 252, clb: 6 },
      { min: 253, max: 279, clb: 7 },
      { min: 280, max: 297, clb: 8 },
      { min: 298, max: 315, clb: 9 },
      { min: 316, max: 360, clb: 10 }
    ],
    reading: [
      { min: 0,   max: 120, clb: 3 },
      { min: 121, max: 150, clb: 4 },
      { min: 151, max: 180, clb: 5 },
      { min: 181, max: 206, clb: 6 },
      { min: 207, max: 232, clb: 7 },
      { min: 233, max: 247, clb: 8 },
      { min: 248, max: 262, clb: 9 },
      { min: 263, max: 300, clb: 10 }
    ],
    writing: [
      { min: 0,   max: 180, clb: 3 },
      { min: 181, max: 225, clb: 4 },
      { min: 226, max: 270, clb: 5 },
      { min: 271, max: 309, clb: 6 },
      { min: 310, max: 348, clb: 7 },
      { min: 349, max: 370, clb: 8 },
      { min: 371, max: 392, clb: 9 },
      { min: 393, max: 450, clb: 10 }
    ]
  },

  TCF: {
    speaking: [
      { min: 0,  max: 3,  clb: 3 },
      { min: 4,  max: 5,  clb: 4 },
      { min: 6,  max: 9,  clb: 5 },
      { min: 10, max: 12, clb: 6 },
      { min: 13, max: 14, clb: 7 },
      { min: 15, max: 16, clb: 8 },
      { min: 17, max: 19, clb: 9 },
      { min: 20, max: 20, clb: 10 }
    ],
    listening: [
      { min: 0,   max: 330, clb: 3 },
      { min: 331, max: 368, clb: 4 },
      { min: 369, max: 397, clb: 5 },
      { min: 398, max: 457, clb: 6 },
      { min: 458, max: 502, clb: 7 },
      { min: 503, max: 540, clb: 8 },
      { min: 541, max: 588, clb: 9 },
      { min: 589, max: 699, clb: 10 }
    ],
    reading: [
      { min: 0,   max: 341, clb: 3 },
      { min: 342, max: 374, clb: 4 },
      { min: 375, max: 405, clb: 5 },
      { min: 406, max: 452, clb: 6 },
      { min: 453, max: 498, clb: 7 },
      { min: 499, max: 523, clb: 8 },
      { min: 524, max: 548, clb: 9 },
      { min: 549, max: 699, clb: 10 }
    ],
    writing: [
      { min: 0,  max: 3,  clb: 3 },
      { min: 4,  max: 5,  clb: 4 },
      { min: 6,  max: 9,  clb: 5 },
      { min: 10, max: 12, clb: 6 },
      { min: 13, max: 14, clb: 7 },
      { min: 15, max: 16, clb: 8 },
      { min: 17, max: 19, clb: 9 },
      { min: 20, max: 20, clb: 10 }
    ]
  }
};

// =========================================================
// HELPER FUNCTIONS
// =========================================================

/**
 * Get CLB level from test score
 */
function getClbFromScore(testType, skill, score) {
  if (!score || score === '' || score === '0') return 0;
  const numScore = parseFloat(score);
  if (isNaN(numScore)) return 0;

  if (testType === 'CELPIP') {
    const map = CLB_CONVERSION.CELPIP[skill];
    if (!map) return 0;
    const clb = map[Math.floor(numScore)];
    return clb || 0;
  }

  // Range-based conversion for IELTS, TEF, TCF
  const ranges = CLB_CONVERSION[testType]?.[skill];
  if (!ranges) return 0;

  for (const range of ranges) {
    if (numScore >= range.min && numScore <= range.max) {
      return range.clb;
    }
  }
  return 0;
}

/**
 * Get language points for first language (CLB → points)
 */
function getLang1Points(clb) {
  const clbCapped = Math.min(Math.max(clb, 0), 10);
  const table = { 0:0, 1:0, 2:0, 3:0, 4:6, 5:6, 6:8, 7:16, 8:22, 9:29, 10:32 };
  return table[clbCapped] || 0;
}

/**
 * Get language points for second language (CLB → points)
 */
function getLang2Points(clb) {
  const table = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:3, 8:3, 9:6, 10:6 };
  const clbCapped = Math.min(Math.max(clb, 0), 10);
  return table[clbCapped] || 0;
}

/**
 * Get spouse language points (CLB → points per skill)
 */
function getSpouseLangPoints(clb) {
  const table = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:3, 8:3, 9:5, 10:5 };
  const clbCapped = Math.min(Math.max(clb, 0), 10);
  return table[clbCapped] || 0;
}

// =========================================================
// MAIN CRS CALCULATION FUNCTION
// =========================================================

function calculateCRS(formData) {

  const hasSpouseComingToCanada = formData.maritalStatus !== 'single'
    && formData.spouseComingToCanada === 'yes';

  const spouseIdx = hasSpouseComingToCanada ? 0 : 1;

  let breakdown = {
    agePoints: 0,
    eduPoints: 0,
    lang1Points: 0,
    lang2Points: 0,
    canadianWEPoints: 0,
    spouseEduPoints: 0,
    spouseLangPoints: 0,
    spouseWEPoints: 0,
    skillTransferPoints: 0,
    additionalPoints: 0
  };

  // ===== SECTION A: CORE HUMAN CAPITAL =====

  // Age
  const ageData = CRS.age[formData.age];
  if (ageData) {
    breakdown.agePoints = ageData[spouseIdx];
  }

  // Education
  const eduData = CRS.education[formData.education];
  if (eduData) {
    breakdown.eduPoints = eduData[spouseIdx];
  }

  // First Official Language (4 skills)
  let lang1CLBs = [];
  if (formData.lang1TestType && formData.lang1TestType !== 'none') {
    const skills = ['speaking', 'listening', 'reading', 'writing'];
    skills.forEach(skill => {
      const clb = getClbFromScore(formData.lang1TestType, skill, formData['lang1_' + skill]);
      lang1CLBs.push(clb);
      breakdown.lang1Points += getLang1Points(clb);
    });
  }
  // Cap first language at max 128 (single) or 128 (with spouse)
  breakdown.lang1Points = Math.min(breakdown.lang1Points, 128);

  // Second Official Language (optional, bonus up to 22 pts)
  let lang2CLBs = [];
  let lang2MinCLB = 0;
  if (formData.lang2TestType && formData.lang2TestType !== 'none') {
    const skills = ['speaking', 'listening', 'reading', 'writing'];
    let lang2PtsRaw = 0;
    skills.forEach(skill => {
      const clb = getClbFromScore(formData.lang2TestType, skill, formData['lang2_' + skill]);
      lang2CLBs.push(clb);
      lang2PtsRaw += getLang2Points(clb);
    });
    breakdown.lang2Points = Math.min(lang2PtsRaw, 22);
    lang2MinCLB = lang2CLBs.length > 0 ? Math.min(...lang2CLBs) : 0;
  }

  // Canadian Work Experience
  const canWE = CRS.canadianWE[String(formData.canadianWE || '0')];
  if (canWE) {
    breakdown.canadianWEPoints = canWE[spouseIdx];
  }

  // ===== SECTION B: SPOUSE/PARTNER FACTORS =====
  if (hasSpouseComingToCanada) {
    // Spouse Education (max 10 pts)
    const spouseEdu = CRS.spouse_education[formData.spouseEducation];
    if (spouseEdu !== undefined) {
      breakdown.spouseEduPoints = Math.min(spouseEdu, 10);
    }

    // Spouse Language (max 20 pts)
    if (formData.spouseLangTestType && formData.spouseLangTestType !== 'none') {
      const skills = ['speaking', 'listening', 'reading', 'writing'];
      let spouseLangPts = 0;
      skills.forEach(skill => {
        const clb = getClbFromScore(formData.spouseLangTestType, skill, formData['spouseLang_' + skill]);
        spouseLangPts += getSpouseLangPoints(clb);
      });
      breakdown.spouseLangPoints = Math.min(spouseLangPts, 20);
    }

    // Spouse Canadian WE (max 10 pts)
    const spouseWEPts = CRS.spouse_canadianWE[String(formData.spouseCanadianWE || '0')];
    if (spouseWEPts !== undefined) {
      breakdown.spouseWEPoints = Math.min(spouseWEPts, 10);
    }
  }

  // ===== SECTION C: SKILL TRANSFERABILITY (max 100 pts total) =====
  let skillTransferRaw = 0;

  // Determine dominant first-language CLB
  const lang1MinCLB = lang1CLBs.length > 0 ? Math.min(...lang1CLBs) : 0;

  // 1. Education + First Language
  if (formData.education !== 'none' && formData.education !== 'secondary') {
    if (lang1MinCLB >= 9) {
      skillTransferRaw += CRS.skillTransfer.educationLang.clb9plus; // 25
    } else if (lang1MinCLB >= 7) {
      skillTransferRaw += CRS.skillTransfer.educationLang.clb7_8;   // 13
    }
  }

  // 2. Education + Foreign Work Experience
  const foreignWE = parseInt(formData.foreignWE || '0');
  if (formData.education !== 'none' && formData.education !== 'secondary') {
    if (foreignWE >= 3) {
      skillTransferRaw += CRS.skillTransfer.educationFWE.three_plus_yr; // 25
    } else if (foreignWE >= 1) {
      skillTransferRaw += CRS.skillTransfer.educationFWE.one_two_yr;    // 13
    }
  }

  // 3. Foreign Work Experience + First Language
  if (foreignWE >= 3) {
    if (lang1MinCLB >= 9) {
      skillTransferRaw += CRS.skillTransfer.foreignWELang.clb9plus; // 25
    } else if (lang1MinCLB >= 7) {
      skillTransferRaw += CRS.skillTransfer.foreignWELang.clb7_8;   // 13
    }
  } else if (foreignWE >= 1) {
    if (lang1MinCLB >= 9) {
      skillTransferRaw += CRS.skillTransfer.foreignWELang.clb9plus; // 25
    } else if (lang1MinCLB >= 7) {
      skillTransferRaw += CRS.skillTransfer.foreignWELang.clb7_8;   // 13
    }
  }

  // 4. Certificate of qualification (trades) + Language
  if (formData.tradeCertificate === 'yes') {
    if (lang1MinCLB >= 7) {
      skillTransferRaw += CRS.skillTransfer.tradesCert.clb7plus; // 25
    } else if (lang1MinCLB >= 5) {
      skillTransferRaw += CRS.skillTransfer.tradesCert.clb5_6;   // 13
    }
  }

  breakdown.skillTransferPoints = Math.min(skillTransferRaw, 100);

  // ===== SECTION D: ADDITIONAL POINTS =====
  let addPts = 0;

  if (formData.pnp === 'yes')
    addPts += CRS.additional.pnp; // 600

  if (formData.jobOfferNOC00 === 'yes')
    addPts += CRS.additional.jobOffer_00; // 200
  else if (formData.jobOfferOther === 'yes')
    addPts += CRS.additional.jobOffer_other; // 50

  if (formData.sibling === 'yes')
    addPts += CRS.additional.sibling; // 15

  // French language bonus
  if (formData.frenchStrongEnglish === 'yes')
    addPts += CRS.additional.french_strong; // 50
  else if (formData.frenchWeakEnglish === 'yes')
    addPts += CRS.additional.french_weak; // 25

  // Canadian post-secondary education
  if (formData.canadianEdu3Plus === 'yes')
    addPts += CRS.additional.canadian_edu_3plus; // 30
  else if (formData.canadianEdu1to2 === 'yes')
    addPts += CRS.additional.canadian_edu_1_2; // 15

  breakdown.additionalPoints = addPts;

  // ===== TOTAL =====
  const coreTotal = breakdown.agePoints + breakdown.eduPoints +
    breakdown.lang1Points + breakdown.lang2Points + breakdown.canadianWEPoints;

  const spouseTotal = breakdown.spouseEduPoints + breakdown.spouseLangPoints +
    breakdown.spouseWEPoints;

  const total = coreTotal + spouseTotal +
    breakdown.skillTransferPoints + breakdown.additionalPoints;

  breakdown.total = Math.min(total, 1200); // Max 1200
  breakdown.coreTotal = coreTotal;
  breakdown.spouseTotal = spouseTotal;

  return breakdown;
}

// =========================================================
// FORM DATA COLLECTION
// =========================================================

function collectFormData(formEl) {
  const fd = new FormData(formEl);
  const data = {};

  // All form field values
  data.age = fd.get('age') || 'under18';
  data.education = fd.get('education') || 'none';
  data.maritalStatus = fd.get('maritalStatus') || 'single';
  data.spouseComingToCanada = fd.get('spouseComingToCanada') || 'no';

  // First language
  data.lang1TestType = fd.get('lang1TestType') || 'none';
  data.lang1_speaking = fd.get('lang1_speaking') || '0';
  data.lang1_listening = fd.get('lang1_listening') || '0';
  data.lang1_reading = fd.get('lang1_reading') || '0';
  data.lang1_writing = fd.get('lang1_writing') || '0';

  // Second language
  data.lang2TestType = fd.get('lang2TestType') || 'none';
  data.lang2_speaking = fd.get('lang2_speaking') || '0';
  data.lang2_listening = fd.get('lang2_listening') || '0';
  data.lang2_reading = fd.get('lang2_reading') || '0';
  data.lang2_writing = fd.get('lang2_writing') || '0';

  // Canadian WE
  data.canadianWE = fd.get('canadianWE') || '0';

  // Spouse
  data.spouseEducation = fd.get('spouseEducation') || 'none';
  data.spouseLangTestType = fd.get('spouseLangTestType') || 'none';
  data.spouseLang_speaking = fd.get('spouseLang_speaking') || '0';
  data.spouseLang_listening = fd.get('spouseLang_listening') || '0';
  data.spouseLang_reading = fd.get('spouseLang_reading') || '0';
  data.spouseLang_writing = fd.get('spouseLang_writing') || '0';
  data.spouseCanadianWE = fd.get('spouseCanadianWE') || '0';

  // Skill transferability
  data.foreignWE = fd.get('foreignWE') || '0';
  data.educationLang = fd.get('educationLang') || 'no';
  data.tradeCertificate = fd.get('tradeCertificate') || 'no';

  // Additional
  data.pnp = fd.get('pnp') || 'no';
  data.jobOfferNOC00 = fd.get('jobOfferNOC00') || 'no';
  data.jobOfferOther = fd.get('jobOfferOther') || 'no';
  data.sibling = fd.get('sibling') || 'no';
  data.frenchStrongEnglish = fd.get('frenchStrongEnglish') || 'no';
  data.frenchWeakEnglish = fd.get('frenchWeakEnglish') || 'no';
  data.canadianEdu1to2 = fd.get('canadianEdu1to2') || 'no';
  data.canadianEdu3Plus = fd.get('canadianEdu3Plus') || 'no';

  return data;
}

// =========================================================
// SCORE DISPLAY
// =========================================================

function getScoreClass(score) {
  if (score >= 500) return 'score-excellent';
  if (score >= 471) return 'score-good';
  if (score >= 451) return 'score-warning';
  if (score >= 400) return 'score-caution';
  return 'score-danger';
}

function getScoreVerdict(score) {
  if (score >= 500) return 'Excellent — Very strong chances of receiving an ITA';
  if (score >= 471) return 'Good — Competitive score for most Express Entry draws';
  if (score >= 451) return 'Moderate — Work on improvements to increase chances';
  if (score >= 400) return 'Low–Moderate — Consider provincial nomination (PNP)';
  return 'Very Low — Significant improvements needed';
}

function getProgressPercent(score) {
  return Math.min((score / 1200) * 100, 100);
}

// Animated count-up
function animateCount(el, target, duration = 1200) {
  const start = 0;
  const step = target / (duration / 16);
  let current = start;
  el.textContent = '0';

  const timer = setInterval(() => {
    current += step;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    el.textContent = Math.round(current);
  }, 16);
}

// =========================================================
// RENDER RESULTS
// =========================================================

function renderResults(breakdown) {
  const resultEl = document.getElementById('crs-results');
  if (!resultEl) return;

  resultEl.classList.add('visible', 'fade-in');

  const scoreClass = getScoreClass(breakdown.total);
  const verdict = getScoreVerdict(breakdown.total);
  const progressPct = getProgressPercent(breakdown.total);

  // Score number with animation
  const scoreNum = resultEl.querySelector('.score-number');
  if (scoreNum) {
    scoreNum.className = 'score-number ' + scoreClass + ' count-up';
    animateCount(scoreNum, breakdown.total);
  }

  // Verdict
  const verdictEl = resultEl.querySelector('.score-verdict');
  if (verdictEl) verdictEl.textContent = verdict;

  // Progress bar
  const progressBar = resultEl.querySelector('.score-progress-fill');
  if (progressBar) {
    progressBar.style.width = '0%';
    setTimeout(() => { progressBar.style.width = progressPct + '%'; }, 100);
  }

  // Score comparison
  const compEl = resultEl.querySelector('.score-comparison');
  if (compEl) {
    compEl.innerHTML = `<strong>Your score of ${breakdown.total}</strong> compares to recent all-program draw cutoffs of approximately 470–525. ${breakdown.total >= 470 ? '✅ You are competitive for current draws!' : '⚠️ Work on improvements to reach the typical cutoff range.'}`;
  }

  // Breakdown table
  const tbodyEl = resultEl.querySelector('#breakdown-tbody');
  if (tbodyEl) {
    tbodyEl.innerHTML = `
      <tr><td>Age</td><td class="breakdown-pts">${breakdown.agePoints}</td></tr>
      <tr><td>Education</td><td class="breakdown-pts">${breakdown.eduPoints}</td></tr>
      <tr><td>First Language (${breakdown.lang1Points > 0 ? 'CLB scored' : 'Not provided'})</td><td class="breakdown-pts">${breakdown.lang1Points}</td></tr>
      <tr><td>Second Language Bonus</td><td class="breakdown-pts">${breakdown.lang2Points}</td></tr>
      <tr><td>Canadian Work Experience</td><td class="breakdown-pts">${breakdown.canadianWEPoints}</td></tr>
      <tr><td colspan="2" style="font-weight:600;color:var(--text-muted);font-size:0.82rem;padding-top:10px;">SPOUSE/PARTNER FACTORS</td></tr>
      <tr><td>Spouse Education</td><td class="breakdown-pts">${breakdown.spouseEduPoints}</td></tr>
      <tr><td>Spouse Language</td><td class="breakdown-pts">${breakdown.spouseLangPoints}</td></tr>
      <tr><td>Spouse Canadian Work Experience</td><td class="breakdown-pts">${breakdown.spouseWEPoints}</td></tr>
      <tr><td colspan="2" style="font-weight:600;color:var(--text-muted);font-size:0.82rem;padding-top:10px;">SKILL TRANSFERABILITY</td></tr>
      <tr><td>Skill Transferability Factors</td><td class="breakdown-pts">${breakdown.skillTransferPoints}</td></tr>
      <tr><td colspan="2" style="font-weight:600;color:var(--text-muted);font-size:0.82rem;padding-top:10px;">ADDITIONAL POINTS</td></tr>
      <tr><td>Additional Points (PNP, Job Offer, etc.)</td><td class="breakdown-pts">${breakdown.additionalPoints}</td></tr>
      <tr class="total-row"><td>TOTAL CRS SCORE</td><td class="breakdown-pts">${breakdown.total}</td></tr>
    `;
  }

  // WhatsApp share
  const waBtn = resultEl.querySelector('.btn-whatsapp');
  if (waBtn) {
    const msg = encodeURIComponent(`I scored ${breakdown.total} on the Canada Express Entry CRS Calculator! Check yours at https://crsscorecalculator.vercel.app`);
    waBtn.href = `https://wa.me/?text=${msg}`;
  }

  // Copy button
  const copyBtn = resultEl.querySelector('.btn-copy');
  if (copyBtn) {
    copyBtn.setAttribute('data-score', breakdown.total);
  }
}

// =========================================================
// FORM INITIALIZATION & EVENT HANDLERS
// =========================================================

function initCalculator() {
  const form = document.getElementById('crs-form');
  if (!form) return;

  // Spouse section toggle
  const maritalRadios = form.querySelectorAll('input[name="maritalStatus"]');
  const spouseSection = document.getElementById('spouse-section');
  const spouseComingSection = document.getElementById('spouse-coming-section');

  function updateSpouseVisibility() {
    const selectedMarital = form.querySelector('input[name="maritalStatus"]:checked');
    const isMarried = selectedMarital && selectedMarital.value !== 'single';

    if (spouseComingSection) {
      spouseComingSection.style.display = isMarried ? 'block' : 'none';
    }

    const spouseComingRadio = form.querySelector('input[name="spouseComingToCanada"]:checked');
    const spouseComing = isMarried && spouseComingRadio && spouseComingRadio.value === 'yes';

    if (spouseSection) {
      spouseSection.classList.toggle('visible', spouseComing);
    }
  }

  maritalRadios.forEach(radio => {
    radio.addEventListener('change', updateSpouseVisibility);
  });

  const spouseComingRadios = form.querySelectorAll('input[name="spouseComingToCanada"]');
  spouseComingRadios.forEach(radio => {
    radio.addEventListener('change', updateSpouseVisibility);
  });

  // Handle radio option styling
  form.querySelectorAll('.radio-option').forEach(option => {
    const radio = option.querySelector('input[type="radio"]');
    if (radio) {
      radio.addEventListener('change', () => {
        // Remove selected from siblings
        const siblings = form.querySelectorAll(`input[name="${radio.name}"]`);
        siblings.forEach(sib => {
          sib.closest('.radio-option')?.classList.remove('selected');
        });
        option.classList.add('selected');
      });
      // Mark initial selection
      if (radio.checked) option.classList.add('selected');
    }
  });

  // Calculate button
  const calcBtn = form.querySelector('.calculate-btn');
  if (calcBtn) {
    calcBtn.addEventListener('click', (e) => {
      e.preventDefault();
      handleCalculate(form);
    });
  }

  // Copy score button
  document.addEventListener('click', (e) => {
    if (e.target.classList.contains('btn-copy') || e.target.closest('.btn-copy')) {
      const btn = e.target.classList.contains('btn-copy') ? e.target : e.target.closest('.btn-copy');
      const score = btn.getAttribute('data-score');
      if (score) {
        navigator.clipboard.writeText(`My CRS Score: ${score} — crsscorecalculator.vercel.app`).then(() => {
          btn.textContent = '✓ Copied!';
          setTimeout(() => { btn.innerHTML = '📋 Copy Score'; }, 2000);
        });
      }
    }
  });

  // Print button
  document.addEventListener('click', (e) => {
    if (e.target.classList.contains('btn-print') || e.target.closest('.btn-print')) {
      window.print();
    }
  });
}

function handleCalculate(form) {
  const formData = collectFormData(form);
  const breakdown = calculateCRS(formData);
  renderResults(breakdown);

  // Auto-scroll to results
  const resultEl = document.getElementById('crs-results');
  if (resultEl) {
    setTimeout(() => {
      resultEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
  }
}

// =========================================================
// INIT ON DOM READY
// =========================================================

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initCalculator);
} else {
  initCalculator();
}
