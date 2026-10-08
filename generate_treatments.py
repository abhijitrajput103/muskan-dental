#!/usr/bin/env python3
"""Generate all treatment HTML pages for Muskan Dental website."""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TREATMENTS_DIR = os.path.join(BASE_DIR, "treatments")

# Treatment data extracted from the website
treatments = [
    {
        "slug": "dental-implants",
        "title": "Dental Implants",
        "page_title": "Dental Implants in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Permanent, pain-free dental implants in Gurgaon by certified implantologists. Single tooth, All-on-4, and computer-guided keyhole implant surgery. Lifetime warranty.",
        "breadcrumb": "Dental Implants",
        "hero_label": "Permanent Tooth Replacement",
        "hero_title": "Advanced Dental Implants<br>in Gurgaon",
        "hero_subtitle": "Dental implants are a long-lasting and natural-looking solution for replacing missing teeth. They restore both function and aesthetics, allowing you to eat, speak, and smile with confidence.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20a%20Dental%20Implants%20consultation.",
        "overview_label": "The Gold Standard",
        "overview_title": "What Are Dental Implants?",
        "overview_text": "Dental implants are one of the most advanced and reliable solutions in modern dentistry. They are designed to replace missing teeth with strong, durable, and natural-looking alternatives that function just like real teeth. A permanent medical-grade titanium or zirconia post anchored directly in the jawbone to replace missing tooth roots. Topped with a lifelike custom ceramic crown, it restores full biting power and never slips.",
        "options_label": "Procedures",
        "options_title": "Options We Offer",
        "options": [
            {"name": "Single Tooth Replacement", "desc": "Replaces one tooth without altering adjacent healthy teeth."},
            {"name": "Implant-Supported Bridge", "desc": "Restores 2–4 consecutive missing teeth on just 2 implants."},
            {"name": "All-on-4 / All-on-6 Arch", "desc": "Full-arch fixed teeth in a day for completely toothless jaws."},
            {"name": "3D Guided Keyhole Surgery", "desc": "Flapless, stitch-free placement with minimal swelling."},
        ],
        "benefits_label": "Advantages",
        "benefits_title": "Why Choose Implants?",
        "benefits": [
            {"title": "100% Chewing Strength", "desc": "Eat apples, nuts, and any favorite foods naturally without slipping."},
            {"title": "Prevents Jawbone Loss", "desc": "Preserves natural facial contours and prevents premature aging."},
            {"title": "Zero Damage to Adjacent Teeth", "desc": "Leaves neighboring natural teeth completely untouched and intact."},
            {"title": "Lifetime Durability", "desc": "98%+ clinical success rate with international warranty systems."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "4-Step Process",
        "process_steps": [
            {"title": "1. 3D Scan & Digital Planning", "desc": "CBCT scan maps bone density and exact implant positioning virtually."},
            {"title": "2. Painless Keyhole Placement", "desc": "Gentle 30-minute procedure under computerized local anesthesia."},
            {"title": "3. Osseointegration & Healing", "desc": "Implant integrates with bone; immediate temporary tooth placed if needed."},
            {"title": "4. Permanent Ceramic Crown", "desc": "Bespoke CAD/CAM crown securely attached for a natural look."},
        ],
        "before_after": [
            {"before": "../before-after/Dental-implants-Bridge01.jpg", "after": "../before-after/Dental-implants-Bridge-after.jpg", "label": "Dental Implant Bridge"},
        ],
        "faqs": [
            {"q": "Does dental implant surgery hurt?", "a": "No. The procedure is performed under effective local anesthesia. Most patients report that getting a dental implant causes significantly less discomfort than a standard tooth extraction. Over-the-counter pain relievers are generally sufficient for the first 24-48 hours."},
            {"q": "How long do dental implants last?", "a": "With good oral hygiene, regular cleanings, and healthy lifestyle habits, dental implants are designed to last for 25+ years to a lifetime. We use internationally certified implant systems that offer official manufacturer warranties."},
            {"q": "Am I a good candidate for dental implants?", "a": "Generally, anyone missing one or more teeth with sufficient jawbone density and healthy gums is an ideal candidate. Even patients with bone loss can receive implants using advanced bone grafting or sinus lift procedures."},
        ],
        "sidebar_time": "30–45 min / implant",
        "sidebar_visits": "2 Visits (or Same-Day)",
        "sidebar_anesthesia": "Painless Computer Local",
        "sidebar_recovery": "24–48 Hours",
        "sidebar_longevity": "Lifetime Durability",
        "doctor": {"name": "Dr. Sudhir Yadav", "title": "Chief Implantologist & Surgeon", "img": "../doctor-sudhir-yadav.jpg", "desc": "Practising since 1998 with 5,000+ successful surgical implant placements in Gurgaon."},
        "related": [
            {"name": "Dental Implant Bridge", "href": "dental-implant-bridge.html"},
            {"name": "E-Max Ceramic Crowns", "href": "e-max-crown.html"},
            {"name": "Anterior Implant", "href": "anterior-implant.html"},
            {"name": "Dental Tourism Packages", "href": "../international.html"},
        ],
        "cta_label": "Reclaim Your Natural Smile",
        "cta_title": "Ready to Replace Missing Teeth<br>Permanently?",
        "cta_text": "Schedule your 3D digital implant consultation today. Dr. Sudhir Yadav and our implantology team are here to guide you toward a lifetime of healthy chewing and confident smiling.",
        "cta_btn_text": "Book Implant Consultation →",
        "hero_img": "../treatments/Dental Implants.jpg",
        "category": "implants",
    },
    {
        "slug": "root-canal",
        "title": "Root Canal Treatment",
        "page_title": "Root Canal Treatment in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Painless single-sitting root canal treatment in Gurgaon with advanced microscopic endodontics. Save your natural tooth with expert precision care.",
        "breadcrumb": "Root Canal Treatment",
        "hero_label": "Save Your Natural Tooth",
        "hero_title": "Painless Root Canal<br>Treatment",
        "hero_subtitle": "Root canal treatment is a painless procedure used to remove infection and save your natural tooth, restoring its function and strength.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20a%20Root%20Canal%20Treatment%20consultation.",
        "overview_label": "Endodontics",
        "overview_title": "What Is Root Canal Treatment?",
        "overview_text": "Root canal treatment is a highly effective dental procedure designed to treat infected or damaged teeth while preserving the natural tooth structure. Using advanced techniques and modern equipment, the infected pulp is carefully removed, and the tooth is cleaned, disinfected, and sealed. This procedure not only eliminates pain but also prevents further infection, helping you maintain your natural smile.",
        "options_label": "Techniques",
        "options_title": "Our Approach",
        "options": [
            {"name": "Microscopic Root Canal", "desc": "Under dental magnification for 100% accuracy in canal cleaning."},
            {"name": "Rotary NiTi Systems", "desc": "Nickel-titanium instruments for faster, gentler canal shaping."},
            {"name": "Single-Sitting RCT", "desc": "Complete root canal in one comfortable visit whenever possible."},
            {"name": "Post & Core + Crown", "desc": "Full strength restoration after root canal with custom ceramic crown."},
        ],
        "benefits_label": "Advantages",
        "benefits_title": "Why Root Canal Treatment?",
        "benefits": [
            {"title": "Save Your Natural Tooth", "desc": "Preserve your natural tooth instead of extraction, maintaining jawbone integrity."},
            {"title": "Completely Painless", "desc": "Advanced anesthesia techniques ensure a comfortable, anxiety-free experience."},
            {"title": "Prevent Infection Spread", "desc": "Eliminate bacteria to stop infection from spreading to other teeth or bone."},
            {"title": "Long-Lasting Results", "desc": "With proper care, a root canal treated tooth can last a lifetime."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "Step-by-Step Process",
        "process_steps": [
            {"title": "1. Digital X-Ray & Diagnosis", "desc": "High-resolution imaging to identify the exact location and extent of infection."},
            {"title": "2. Painless Numbing", "desc": "Computer-controlled anesthesia for a completely comfortable experience."},
            {"title": "3. Pulp Removal & Cleaning", "desc": "Infected tissue removed, canals shaped and disinfected under magnification."},
            {"title": "4. Sealing & Crown Placement", "desc": "Canal sealed with biocompatible material and protected with a ceramic crown."},
        ],
        "before_after": [],
        "faqs": [
            {"q": "Is root canal treatment painful?", "a": "No. Modern root canal procedures are performed under effective local anesthesia and are virtually painless. Most patients feel only mild pressure during the procedure."},
            {"q": "How many visits does it take?", "a": "Most root canal treatments can be completed in a single sitting of 45–60 minutes. Complex cases may require a second visit."},
            {"q": "What happens after root canal treatment?", "a": "A ceramic crown is placed over the treated tooth to protect and strengthen it. With proper oral hygiene, the tooth can last a lifetime."},
        ],
        "sidebar_time": "45–60 minutes",
        "sidebar_visits": "Single Sitting",
        "sidebar_anesthesia": "Painless Local",
        "sidebar_recovery": "Immediate",
        "sidebar_longevity": "Lifetime with Crown",
        "doctor": {"name": "Dr. Sudhir Yadav", "title": "Endodontic Specialist", "img": "../doctor-sudhir-yadav.jpg", "desc": "Expert in microscopic root canal treatment with thousands of successful procedures in Gurgaon."},
        "related": [
            {"name": "E-Max Ceramic Crowns", "href": "e-max-crown.html"},
            {"name": "E-Max Endocrown", "href": "e-max-endocrown.html"},
            {"name": "General Dentistry", "href": "general-dentistry.html"},
        ],
        "cta_label": "Save Your Natural Tooth",
        "cta_title": "Experiencing Tooth Pain?<br>Get Relief Today",
        "cta_text": "Don't let a toothache ruin your day. Our painless root canal treatment can save your tooth and eliminate pain in a single comfortable visit.",
        "cta_btn_text": "Book Root Canal Consultation →",
        "hero_img": "../treatments/Root Canal.jpg",
        "category": "general",
    },
    {
        "slug": "smile-makeover",
        "title": "Smile Makeover",
        "page_title": "Smile Makeover in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Transform your smile with a personalized smile makeover at Muskan Dental. Veneers, whitening, crowns, and digital smile design for a stunning smile.",
        "breadcrumb": "Smile Makeover",
        "hero_label": "Complete Smile Transformation",
        "hero_title": "Smile Makeover<br>in Gurgaon",
        "hero_subtitle": "A smile makeover is a customized combination of treatments designed to enhance the appearance of your smile and boost confidence.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20a%20Smile%20Makeover%20consultation.",
        "overview_label": "Cosmetic Excellence",
        "overview_title": "What Is a Smile Makeover?",
        "overview_text": "A smile makeover is a personalized dental treatment plan that combines multiple cosmetic procedures to improve the overall appearance of your smile. Depending on your needs, it may include teeth whitening, veneers, crowns, or orthodontic treatments. Using advanced techniques and aesthetic planning, we create a natural, balanced, and confident smile tailored specifically for you.",
        "options_label": "Procedures",
        "options_title": "Treatments Included",
        "options": [
            {"name": "Porcelain Veneers", "desc": "Ultra-thin shells to reshape, whiten, and perfect your smile."},
            {"name": "Teeth Whitening", "desc": "Professional brightening to restore your natural radiance."},
            {"name": "Dental Crowns", "desc": "Full coverage restorations for damaged or misshapen teeth."},
            {"name": "Digital Smile Design", "desc": "3D preview of your new smile before treatment begins."},
        ],
        "benefits_label": "Advantages",
        "benefits_title": "Why Choose a Smile Makeover?",
        "benefits": [
            {"title": "Personalized Treatment Plan", "desc": "Every smile makeover is custom-designed to match your facial features and preferences."},
            {"title": "Boost Confidence", "desc": "A beautiful smile transforms your self-esteem and social interactions."},
            {"title": "Natural-Looking Results", "desc": "Modern materials and techniques ensure results that look completely natural."},
            {"title": "Comprehensive Solution", "desc": "Address multiple cosmetic concerns in one coordinated treatment plan."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "Your Smile Makeover Journey",
        "process_steps": [
            {"title": "1. Smile Assessment & Design", "desc": "Comprehensive evaluation and digital smile design preview of your new look."},
            {"title": "2. Treatment Planning", "desc": "Customized plan combining the ideal procedures for your goals."},
            {"title": "3. Step-by-Step Execution", "desc": "Each procedure performed with precision for optimal results."},
            {"title": "4. Final Reveal", "desc": "Your stunning new smile unveiled — ready to make an impression."},
        ],
        "before_after": [],
        "faqs": [
            {"q": "How long does a smile makeover take?", "a": "Depending on the procedures involved, a smile makeover can take from 2 visits to several weeks. Many cosmetic treatments can be completed in just a few days."},
            {"q": "Is a smile makeover permanent?", "a": "Porcelain veneers and crowns are long-lasting (15+ years). Teeth whitening may require periodic touch-ups. We provide complete aftercare guidance."},
            {"q": "Will it look natural?", "a": "Absolutely. We use the latest digital smile design technology and premium materials to create results that look completely natural and harmonious."},
        ],
        "sidebar_time": "Varies by treatment",
        "sidebar_visits": "2-4 Visits",
        "sidebar_anesthesia": "Painless Local",
        "sidebar_recovery": "Minimal to None",
        "sidebar_longevity": "15+ Years",
        "doctor": {"name": "Dr. Archana Yadav", "title": "Cosmetic Dentistry Specialist", "img": "../doctor-archana-yadav.jpg", "desc": "Expert in digital smile design and cosmetic transformations for patients worldwide."},
        "related": [
            {"name": "Veneers", "href": "veneers.html"},
            {"name": "Teeth Whitening", "href": "teeth-whitening.html"},
            {"name": "E-Max Ceramic Crowns", "href": "e-max-crown.html"},
        ],
        "cta_label": "Your Dream Smile Awaits",
        "cta_title": "Ready for Your<br>Smile Transformation?",
        "cta_text": "Book your smile design consultation today and see a 3D preview of your new smile before treatment begins.",
        "cta_btn_text": "Book Smile Consultation →",
        "hero_img": "../treatments/Esthetic Dentistry.jpg",
        "category": "cosmetic",
    },
    {
        "slug": "veneers",
        "title": "Veneers",
        "page_title": "Porcelain Veneers in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Premium porcelain veneers in Gurgaon for a flawless, natural smile. Custom-designed ultra-thin shells to correct stains, gaps, chips, and misalignment.",
        "breadcrumb": "Veneers",
        "hero_label": "Flawless Smile Design",
        "hero_title": "Porcelain Veneers<br>in Gurgaon",
        "hero_subtitle": "Veneers are thin custom-made shells that enhance the shape, color, and alignment of your teeth for a flawless smile.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20a%20Veneers%20consultation.",
        "overview_label": "Cosmetic Dentistry",
        "overview_title": "What Are Dental Veneers?",
        "overview_text": "Veneers are ultra-thin, custom-designed shells made from porcelain or composite material that are bonded to the front surface of your teeth. They are an ideal solution for correcting imperfections such as stains, gaps, chips, or misalignment. Veneers provide a natural, long-lasting, and aesthetically pleasing smile transformation with minimal tooth preparation.",
        "options_label": "Types",
        "options_title": "Veneer Options We Offer",
        "options": [
            {"name": "Porcelain Veneers", "desc": "Premium ceramic shells with lifelike translucency and 15+ year durability."},
            {"name": "E-Max Veneers", "desc": "High-strength lithium disilicate for the most natural appearance."},
            {"name": "Composite Veneers", "desc": "Budget-friendly option with same-day application and good aesthetics."},
            {"name": "Minimal Prep Veneers", "desc": "Ultra-thin design requiring minimal to no tooth reduction."},
        ],
        "benefits_label": "Advantages",
        "benefits_title": "Why Choose Veneers?",
        "benefits": [
            {"title": "Instant Smile Transformation", "desc": "Correct multiple imperfections — stains, gaps, chips — in just 2 visits."},
            {"title": "Natural Appearance", "desc": "Porcelain mimics the light-reflecting properties of natural tooth enamel."},
            {"title": "Stain Resistant", "desc": "Porcelain veneers resist coffee, tea, and wine stains permanently."},
            {"title": "Minimal Tooth Preparation", "desc": "Preserve maximum natural tooth structure with ultra-thin designs."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "Veneer Placement Process",
        "process_steps": [
            {"title": "1. Smile Assessment & Design", "desc": "Digital smile analysis and shade selection for your perfect veneers."},
            {"title": "2. Tooth Preparation", "desc": "Minimal enamel reduction to create space for the ultra-thin veneer."},
            {"title": "3. Custom Fabrication", "desc": "Lab-crafted veneers designed to match your natural teeth perfectly."},
            {"title": "4. Precision Bonding", "desc": "Veneers permanently bonded for a stunning, natural-looking smile."},
        ],
        "before_after": [
            {"before": "../before-after/veneers-before.jpg", "after": "../before-after/veneers-after.jpg", "label": "Porcelain Veneers"},
            {"before": "../before-after/E max veneer-before.jpeg", "after": "../before-after/E max veneer-after.jpeg", "label": "E-Max Veneers"},
        ],
        "faqs": [
            {"q": "How long do veneers last?", "a": "Porcelain veneers typically last 15-20 years with proper care. Composite veneers may last 5-7 years before requiring replacement."},
            {"q": "Do veneers look natural?", "a": "Yes, modern porcelain veneers are custom-designed to match the color, shape, and translucency of your natural teeth, making them virtually undetectable."},
            {"q": "Is the procedure painful?", "a": "The procedure is performed under local anesthesia and is completely painless. Most patients feel only mild sensitivity for a day or two after placement."},
        ],
        "sidebar_time": "60–90 min per session",
        "sidebar_visits": "2 Visits",
        "sidebar_anesthesia": "Painless Local",
        "sidebar_recovery": "Immediate",
        "sidebar_longevity": "15–20 Years",
        "doctor": {"name": "Dr. Archana Yadav", "title": "Cosmetic Dentistry Specialist", "img": "../doctor-archana-yadav.jpg", "desc": "Expert in porcelain veneer placement and digital smile design with hundreds of successful transformations."},
        "related": [
            {"name": "Smile Makeover", "href": "smile-makeover.html"},
            {"name": "Teeth Whitening", "href": "teeth-whitening.html"},
            {"name": "E-Max Ceramic Crowns", "href": "e-max-crown.html"},
        ],
        "cta_label": "Your Perfect Smile Awaits",
        "cta_title": "Ready for a Flawless<br>Smile?",
        "cta_text": "Book your veneer consultation today and discover how custom veneers can transform your smile in just two visits.",
        "cta_btn_text": "Book Veneer Consultation →",
        "hero_img": "../before-after/veneers-after.jpg",
        "category": "cosmetic",
    },
    {
        "slug": "dental-crowns-bridges",
        "title": "Dental Crowns & Bridges",
        "page_title": "Dental Crowns & Bridges in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Expert dental crown and bridge treatment in Gurgaon. Restore damaged or missing teeth with durable, natural-looking ceramic restorations.",
        "breadcrumb": "Dental Crowns & Bridges",
        "hero_label": "Restorative Dentistry",
        "hero_title": "Dental Crowns & Bridges<br>in Gurgaon",
        "hero_subtitle": "Dental crowns and bridges are effective solutions to restore damaged or missing teeth, improving both function and appearance.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20a%20Dental%20Crowns%20consultation.",
        "overview_label": "Restorative Care",
        "overview_title": "What Are Crowns & Bridges?",
        "overview_text": "Dental crowns and bridges are commonly used restorative treatments designed to repair damaged teeth or replace missing ones. A crown is placed over a weakened or broken tooth to restore its strength, shape, and appearance, while a bridge is used to fill the gap created by one or more missing teeth. These treatments not only improve functionality but also enhance your smile and overall oral health.",
        "options_label": "Types",
        "options_title": "Options Available",
        "options": [
            {"name": "Porcelain Crowns", "desc": "All-ceramic crowns that match natural teeth for front tooth restorations."},
            {"name": "PFM Crowns", "desc": "Porcelain-fused-to-metal for excellent strength in back teeth."},
            {"name": "Zirconia Crowns", "desc": "Ultra-strong ceramic crowns for maximum durability and aesthetics."},
            {"name": "Fixed Bridges", "desc": "Replace one or more missing teeth anchored to adjacent natural teeth."},
        ],
        "benefits_label": "Advantages",
        "benefits_title": "Why Choose Crowns & Bridges?",
        "benefits": [
            {"title": "Restore Function", "desc": "Eat and speak normally with fully functional restorations."},
            {"title": "Natural Appearance", "desc": "Modern ceramic materials provide lifelike aesthetics."},
            {"title": "Protect Damaged Teeth", "desc": "Crowns shield weakened teeth from further damage or fracture."},
            {"title": "Fill Gaps Permanently", "desc": "Bridges replace missing teeth without removable dentures."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "Crown & Bridge Process",
        "process_steps": [
            {"title": "1. Examination & Planning", "desc": "Thorough assessment with X-rays and digital impressions."},
            {"title": "2. Tooth Preparation", "desc": "The tooth is shaped to accommodate the crown or bridge."},
            {"title": "3. Custom Fabrication", "desc": "Lab-crafted restoration matched to your natural teeth."},
            {"title": "4. Final Cementation", "desc": "Precision fitting and permanent bonding for lasting results."},
        ],
        "before_after": [],
        "faqs": [
            {"q": "How long do crowns and bridges last?", "a": "With proper care and regular dental visits, crowns and bridges typically last 10-15 years, and many last even longer."},
            {"q": "Is the procedure painful?", "a": "The procedure is performed under local anesthesia and is completely painless. A temporary crown is placed while your permanent one is being made."},
            {"q": "Can I eat normally with a crown or bridge?", "a": "Yes. Once cemented, crowns and bridges function like natural teeth. You can eat, speak, and smile with full confidence."},
        ],
        "sidebar_time": "45–60 minutes",
        "sidebar_visits": "2 Visits",
        "sidebar_anesthesia": "Painless Local",
        "sidebar_recovery": "Immediate",
        "sidebar_longevity": "10–15+ Years",
        "doctor": {"name": "Dr. Sudhir Yadav", "title": "Prosthodontic Specialist", "img": "../doctor-sudhir-yadav.jpg", "desc": "Expert in restorative dentistry with decades of experience in crown and bridge treatments."},
        "related": [
            {"name": "E-Max Ceramic Crowns", "href": "e-max-crown.html"},
            {"name": "Dental Implants", "href": "dental-implants.html"},
            {"name": "Anterior PFM Bridge", "href": "anterior-pfm-bridge.html"},
        ],
        "cta_label": "Restore Your Smile",
        "cta_title": "Need a Crown or Bridge?<br>We Can Help",
        "cta_text": "Book your consultation today and let our experts restore your damaged or missing teeth with premium quality restorations.",
        "cta_btn_text": "Book Crown Consultation →",
        "hero_img": "../treatments/Esthetic Dentistry.jpg",
        "category": "implants",
    },
    {
        "slug": "teeth-whitening",
        "title": "Teeth Whitening",
        "page_title": "Teeth Whitening in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Professional teeth whitening in Gurgaon. Safe, effective laser whitening to brighten your smile up to 8 shades in a single 60-minute session.",
        "breadcrumb": "Teeth Whitening",
        "hero_label": "Cosmetic Brightening",
        "hero_title": "Professional Teeth<br>Whitening",
        "hero_subtitle": "Teeth whitening is a safe and effective treatment that removes stains and restores the natural brightness of your smile.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20a%20Teeth%20Whitening%20appointment.",
        "overview_label": "Cosmetic Care",
        "overview_title": "What Is Teeth Whitening?",
        "overview_text": "Teeth whitening is one of the most popular cosmetic dental treatments designed to enhance the brightness of your smile. Over time, teeth can become stained due to food, beverages, smoking, or aging. Our professional whitening treatments use advanced techniques to safely remove stains and lighten the color of your teeth, giving you a noticeably brighter and more confident smile in a short time.",
        "options_label": "Methods",
        "options_title": "Whitening Options",
        "options": [
            {"name": "Laser Whitening", "desc": "Advanced in-office treatment for dramatic results in one session."},
            {"name": "Philips Zoom Whitening", "desc": "Clinically proven system for up to 8 shades brighter in 60 minutes."},
            {"name": "Custom Take-Home Trays", "desc": "Professional-grade whitening gel with custom-fitted trays for home use."},
            {"name": "Combination Treatment", "desc": "In-office + take-home for maximum and long-lasting brightness."},
        ],
        "benefits_label": "Advantages",
        "benefits_title": "Why Professional Whitening?",
        "benefits": [
            {"title": "Dramatic Results Fast", "desc": "Up to 8 shades brighter in a single comfortable 60-minute session."},
            {"title": "Safe & Enamel-Friendly", "desc": "Professional-grade formulas that protect enamel while removing stains."},
            {"title": "Long-Lasting Brightness", "desc": "Results last months to years with simple at-home maintenance."},
            {"title": "Boosts Confidence", "desc": "A bright, white smile makes a lasting first impression."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "Whitening Process",
        "process_steps": [
            {"title": "1. Shade Assessment", "desc": "Current shade documented and target brightness determined."},
            {"title": "2. Gum Protection", "desc": "Protective barriers applied to safeguard gums and soft tissue."},
            {"title": "3. Whitening Application", "desc": "Professional gel applied and activated with laser or LED light."},
            {"title": "4. Final Results", "desc": "Immediate visible results with aftercare guidance provided."},
        ],
        "before_after": [],
        "faqs": [
            {"q": "Is teeth whitening safe?", "a": "Yes. Professional teeth whitening under dental supervision is completely safe and does not damage tooth enamel. We use clinically proven formulas."},
            {"q": "How long does whitening last?", "a": "Results typically last 6 months to 2 years depending on your diet and habits. Touch-up treatments can extend the results."},
            {"q": "Will whitening make my teeth sensitive?", "a": "Mild temporary sensitivity is normal and usually subsides within 24-48 hours. We use desensitizing agents to minimize discomfort."},
        ],
        "sidebar_time": "60 minutes",
        "sidebar_visits": "Single Visit",
        "sidebar_anesthesia": "None Required",
        "sidebar_recovery": "Immediate",
        "sidebar_longevity": "6 Months – 2 Years",
        "doctor": {"name": "Dr. Archana Yadav", "title": "Cosmetic Dentistry Specialist", "img": "../doctor-archana-yadav.jpg", "desc": "Expert in professional teeth whitening treatments with hundreds of happy, bright smiles."},
        "related": [
            {"name": "Smile Makeover", "href": "smile-makeover.html"},
            {"name": "Veneers", "href": "veneers.html"},
            {"name": "Cosmetic Dentistry", "href": "cosmetic-dentistry.html"},
        ],
        "cta_label": "Brighten Your Smile",
        "cta_title": "Ready for a Brighter,<br>Whiter Smile?",
        "cta_text": "Book your professional teeth whitening session today and walk out with a dramatically brighter smile in just one hour.",
        "cta_btn_text": "Book Whitening Session →",
        "hero_img": "../treatments/Esthetic Dentistry.jpg",
        "category": "cosmetic",
    },
    {
        "slug": "kids-dentistry",
        "title": "Pediatric Dentistry",
        "page_title": "Pediatric Dentistry in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Gentle, child-friendly pediatric dentistry in Gurgaon. Expert care for children including fluoride treatment, sealants, and early orthodontic guidance.",
        "breadcrumb": "Pediatric Dentistry",
        "hero_label": "Child-Friendly Dental Care",
        "hero_title": "Pediatric Dentistry<br>in Gurgaon",
        "hero_subtitle": "Specialized dental care for children in a gentle, fun, and welcoming environment. Building healthy smiles from the start.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20a%20Pediatric%20Dentistry%20appointment%20for%20my%20child.",
        "overview_label": "Kids Care",
        "overview_title": "What Is Pediatric Dentistry?",
        "overview_text": "Pediatric dentistry focuses on the oral health of children from infancy through adolescence. Our pediatric specialists create a warm, stress-free environment to help children develop positive dental habits early. From routine check-ups and fluoride applications to cavity treatments and early orthodontic assessments, we provide comprehensive care tailored to growing smiles.",
        "options_label": "Services",
        "options_title": "Pediatric Services",
        "options": [
            {"name": "Fluoride Applications", "desc": "Professional fluoride treatment to strengthen developing tooth enamel."},
            {"name": "Pit & Fissure Sealants", "desc": "Protective sealants on molars to prevent cavities in grooves."},
            {"name": "Child-Friendly Fillings", "desc": "Tooth-colored composite fillings for natural-looking cavity repair."},
            {"name": "Early Orthodontic Guidance", "desc": "Assessment and interceptive treatment for developing bite issues."},
        ],
        "benefits_label": "Advantages",
        "benefits_title": "Why Choose Us for Your Child?",
        "benefits": [
            {"title": "Gentle & Caring Approach", "desc": "Our specialists use behavior management techniques to keep kids calm and happy."},
            {"title": "Child-Friendly Environment", "desc": "Fun, colorful clinic designed to make dental visits enjoyable for children."},
            {"title": "Preventive Focus", "desc": "Emphasis on prevention to avoid complex treatments later in life."},
            {"title": "Expert Pediatric Team", "desc": "Specialized training in treating children of all ages and temperaments."},
        ],
        "process_label": "Visit Journey",
        "process_title": "Your Child's Dental Visit",
        "process_steps": [
            {"title": "1. Welcome & Familiarization", "desc": "Child-friendly introduction to the clinic and dental team."},
            {"title": "2. Gentle Examination", "desc": "Comprehensive check-up with digital X-rays if needed."},
            {"title": "3. Preventive Treatment", "desc": "Fluoride, sealants, or gentle cleaning as recommended."},
            {"title": "4. Oral Health Education", "desc": "Fun brushing and flossing tips for parents and children."},
        ],
        "before_after": [],
        "faqs": [
            {"q": "At what age should my child first visit the dentist?", "a": "We recommend bringing your child for their first dental visit by age 1 or within 6 months of their first tooth eruption."},
            {"q": "How do you handle anxious children?", "a": "Our pediatric specialists use gentle behavior management techniques, distraction methods, and a fun environment to make dental visits stress-free."},
            {"q": "Are dental X-rays safe for children?", "a": "Yes. We use low-dose digital X-rays that emit minimal radiation, far less than traditional X-rays, ensuring safety for young patients."},
        ],
        "sidebar_time": "20–30 minutes",
        "sidebar_visits": "Regular Check-ups",
        "sidebar_anesthesia": "Gentle & Pain-Free",
        "sidebar_recovery": "Immediate",
        "sidebar_longevity": "Ongoing Care",
        "doctor": {"name": "Dr. Archana Yadav", "title": "Pediatric Dentistry Specialist", "img": "../doctor-archana-yadav.jpg", "desc": "Compassionate pediatric dental specialist dedicated to making every child's dental experience positive and fun."},
        "related": [
            {"name": "Orthodontics & Aligners", "href": "orthodontics.html"},
            {"name": "General Dentistry", "href": "general-dentistry.html"},
            {"name": "Teeth Whitening", "href": "teeth-whitening.html"},
        ],
        "cta_label": "Your Child's Healthy Smile Starts Here",
        "cta_title": "Schedule Your Child's<br>Dental Visit Today",
        "cta_text": "Give your child the gift of a healthy smile. Book a gentle, fun dental check-up with our pediatric specialists.",
        "cta_btn_text": "Book Kids Appointment →",
        "hero_img": "../treatments/Kids Dentistry.jpg",
        "category": "ortho",
    },
    {
        "slug": "orthodontics",
        "title": "Orthodontics",
        "page_title": "Orthodontics & Clear Aligners in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Expert orthodontic treatment in Gurgaon. Braces, clear aligners, and invisible orthodontics for straighter teeth and a perfect smile.",
        "breadcrumb": "Orthodontics",
        "hero_label": "Straight Teeth, Perfect Bite",
        "hero_title": "Orthodontics & Clear<br>Aligners",
        "hero_subtitle": "Orthodontic treatments help correct misaligned teeth and bite issues using braces or aligners for a healthier and more confident smile.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20an%20Orthodontic%20consultation.",
        "overview_label": "Orthodontic Care",
        "overview_title": "What Is Orthodontic Treatment?",
        "overview_text": "Orthodontics focuses on correcting the alignment of teeth and jaws to improve both function and appearance. Whether through traditional braces or modern clear aligners, these treatments gradually move teeth into their ideal position. With advanced techniques and personalized treatment planning, orthodontics helps create a balanced, healthy, and aesthetically pleasing smile.",
        "options_label": "Options",
        "options_title": "Treatment Options",
        "options": [
            {"name": "Metal Braces", "desc": "Traditional fixed braces with modern low-profile brackets for effective alignment."},
            {"name": "Ceramic Braces", "desc": "Tooth-colored brackets that blend naturally for a discreet appearance."},
            {"name": "Clear Aligners", "desc": "Invisible, removable trays that straighten teeth without wires."},
            {"name": "Self-Ligating Braces", "desc": "Advanced braces requiring fewer adjustments and shorter treatment time."},
        ],
        "benefits_label": "Advantages",
        "benefits_title": "Why Choose Orthodontic Treatment?",
        "benefits": [
            {"title": "Straighter Teeth", "desc": "Correct crowding, gaps, and crooked teeth for a beautiful smile."},
            {"title": "Improved Bite Function", "desc": "Fix overbite, underbite, and crossbite for better chewing and speech."},
            {"title": "Better Oral Health", "desc": "Aligned teeth are easier to clean, reducing risk of cavities and gum disease."},
            {"title": "Boosted Confidence", "desc": "A straight, aligned smile significantly improves self-confidence."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "Orthodontic Process",
        "process_steps": [
            {"title": "1. Comprehensive Assessment", "desc": "Digital scans, X-rays, and photos for complete orthodontic analysis."},
            {"title": "2. Custom Treatment Plan", "desc": "Personalized plan with projected timeline and expected results."},
            {"title": "3. Braces/Aligner Placement", "desc": "Comfortable placement with detailed care instructions."},
            {"title": "4. Regular Adjustments", "desc": "Periodic visits for adjustments and progress monitoring."},
        ],
        "before_after": [],
        "faqs": [
            {"q": "How long does orthodontic treatment take?", "a": "Treatment duration varies from 6 months to 24 months depending on the complexity of your case. Clear aligner cases often finish faster."},
            {"q": "Are clear aligners effective?", "a": "Yes. Modern clear aligners can treat most orthodontic cases effectively, including crowding, spacing, and mild to moderate bite issues."},
            {"q": "Is orthodontic treatment painful?", "a": "There may be mild discomfort for 2-3 days after placement and adjustments, but it is very manageable and subsides quickly."},
        ],
        "sidebar_time": "6–24 months",
        "sidebar_visits": "Monthly Adjustments",
        "sidebar_anesthesia": "None Required",
        "sidebar_recovery": "No Downtime",
        "sidebar_longevity": "Permanent Results",
        "doctor": {"name": "Dr. Varun Dahiya", "title": "Orthodontic Specialist", "img": "../doctor-varun-dahiya.jpg", "desc": "Specialist in orthodontics with expertise in clear aligners and advanced bracket systems."},
        "related": [
            {"name": "Pediatric Dentistry", "href": "kids-dentistry.html"},
            {"name": "Smile Makeover", "href": "smile-makeover.html"},
            {"name": "Veneers", "href": "veneers.html"},
        ],
        "cta_label": "Straighten Your Smile",
        "cta_title": "Ready for Straighter,<br>More Confident Teeth?",
        "cta_text": "Book your orthodontic consultation today and discover the best treatment option for your perfect smile.",
        "cta_btn_text": "Book Ortho Consultation →",
        "hero_img": "../treatments/Orthodontic Braces.jpg",
        "category": "ortho",
    },
    {
        "slug": "e-max-endocrown",
        "title": "E-Max Endocrown",
        "page_title": "E-Max Endocrown in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Premium E-Max endocrown restorations in Gurgaon. High-strength lithium disilicate ceramic for root canal treated teeth without posts or cores.",
        "breadcrumb": "E-Max Endocrown",
        "hero_label": "Advanced Ceramic Restoration",
        "hero_title": "E-Max Endocrown<br>Treatment",
        "hero_subtitle": "An all-in-one, high-strength lithium disilicate (E-max) restoration designed specifically for root canal-treated teeth, anchoring directly inside the pulp chamber without requiring a post or core build-up.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20an%20E-Max%20Endocrown%20consultation.",
        "overview_label": "Ceramic Technology",
        "overview_title": "What Is an E-Max Endocrown?",
        "overview_text": "E-max Endocrowns provide a modern, minimally invasive alternative to traditional post-and-core supported full crowns for post-endodontic restorations. Fabricated from a single block of high-strength lithium disilicate glass-ceramic, an endocrown utilizes the internal geometry of the cleaned pulp chamber for retention. By retaining remaining coronal tooth structure and eliminating the mechanical stress associated with metal or fiber posts, E-max endocrowns offer superior resistance to fracture, excellent marginal integrity, and exceptional long-term structural integrity for heavily restored posterior teeth.",
        "options_label": "Advantages",
        "options_title": "Key Features",
        "options": [
            {"name": "No Post Required", "desc": "Anchors directly in the pulp chamber, eliminating post-related stress."},
            {"name": "Monolithic Construction", "desc": "Single-block fabrication for maximum strength and resistance to fracture."},
            {"name": "Preserves Tooth Structure", "desc": "Retains maximum remaining tooth for long-term structural integrity."},
            {"name": "Superior Aesthetics", "desc": "High translucency matches natural teeth perfectly in visible areas."},
        ],
        "benefits_label": "Benefits",
        "benefits_title": "Why Choose E-Max Endocrown?",
        "benefits": [
            {"title": "Maximum Strength", "desc": "Lithium disilicate provides exceptional fracture resistance for posterior teeth."},
            {"title": "Minimally Invasive", "desc": "No root canal post needed — less drilling, more tooth preserved."},
            {"title": "Natural Aesthetics", "desc": "Translucent ceramic blends seamlessly with natural tooth structure."},
            {"title": "Long-Term Reliability", "desc": "Excellent marginal seal and structural integrity for decades of use."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "Endocrown Procedure",
        "process_steps": [
            {"title": "1. Post-RCT Assessment", "desc": "Evaluation of root canal treated tooth and pulp chamber geometry."},
            {"title": "2. Digital Impression", "desc": "Precise digital scan of the prepared tooth and pulp chamber."},
            {"title": "3. CAD/CAM Fabrication", "desc": "Computer-designed and milled from a single E-max ceramic block."},
            {"title": "4. Adhesive Bonding", "desc": "Precision bonding with resin cement for a permanent, sealed fit."},
        ],
        "before_after": [
            {"before": "../before-after/emax-endocrown.jpeg", "after": "../before-after/emax-endocrown2.jpeg", "label": "E-Max Endocrown"},
        ],
        "faqs": [
            {"q": "What is the difference between a crown and an endocrown?", "a": "A traditional crown requires a post inside the root canal for support, while an endocrown anchors directly in the pulp chamber, preserving more tooth structure."},
            {"q": "Is an endocrown as strong as a regular crown?", "a": "Yes. Studies show E-max endocrowns provide equal or superior fracture resistance compared to post-supported crowns, especially in posterior teeth."},
            {"q": "How long does an endocrown last?", "a": "With proper oral care, E-max endocrowns can last 15+ years. The adhesive bonding provides excellent long-term stability."},
        ],
        "sidebar_time": "45–60 minutes",
        "sidebar_visits": "2 Visits",
        "sidebar_anesthesia": "Minimal/None",
        "sidebar_recovery": "Immediate",
        "sidebar_longevity": "15+ Years",
        "doctor": {"name": "Dr. Sudhir Yadav", "title": "Prosthodontic Specialist", "img": "../doctor-sudhir-yadav.jpg", "desc": "Expert in advanced ceramic restorations and CAD/CAM dentistry for precision outcomes."},
        "related": [
            {"name": "E-Max Crown", "href": "e-max-crown.html"},
            {"name": "E-Max Inlay", "href": "e-max-inlay.html"},
            {"name": "Root Canal Treatment", "href": "root-canal.html"},
        ],
        "cta_label": "Premium Ceramic Restorations",
        "cta_title": "Need a Restoration After<br>Root Canal?",
        "cta_text": "Discover the E-max endocrown — the modern, minimally invasive alternative that preserves your tooth while providing lasting strength.",
        "cta_btn_text": "Book Endocrown Consultation →",
        "hero_img": "../before-after/emax-endocrown2.jpeg",
        "category": "implants",
    },
    {
        "slug": "e-max-inlay",
        "title": "E-Max Inlay",
        "page_title": "E-Max Inlay in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Premium E-Max inlay restorations in Gurgaon. Custom-milled ceramic inlays for precise, durable, and natural-looking cavity restoration.",
        "breadcrumb": "E-Max Inlay",
        "hero_label": "Minimally Invasive Restoration",
        "hero_title": "E-Max Inlay<br>Treatment",
        "hero_subtitle": "A durable, custom-milled lithium disilicate (E-max) ceramic restoration designed to fit precisely within damaged cusps, reinforcing natural tooth structure without full crown coverage.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20an%20E-Max%20Inlay%20consultation.",
        "overview_label": "Conservative Dentistry",
        "overview_title": "What Is an E-Max Inlay?",
        "overview_text": "E-max Inlays offer an advanced, minimally invasive solution for restoring posterior teeth with moderate decay or fracture. Crafted from high-strength lithium disilicate glass-ceramic, E-max inlays fit tightly into the prepared tooth cavity like a precise puzzle piece, restoring full natural aesthetics and structural integrity. By preserving significantly more natural enamel and dentin than full crowns, E-max inlays provide high translucency, exceptional wear resistance, and long-term durability under heavy chewing forces.",
        "options_label": "Types",
        "options_title": "Inlay Options",
        "options": [
            {"name": "E-Max Inlay", "desc": "Fits within the cusps of the tooth for moderate cavity restorations."},
            {"name": "E-Max Onlay", "desc": "Covers one or more cusps for more extensive damage repair."},
            {"name": "CAD/CAM Precision", "desc": "Computer-designed and milled for perfect fit and function."},
            {"name": "Adhesive Bonding", "desc": "Resin cement creates a seamless, leak-proof seal."},
        ],
        "benefits_label": "Benefits",
        "benefits_title": "Why Choose E-Max Inlays?",
        "benefits": [
            {"title": "Preserves Natural Tooth", "desc": "Removes less tooth structure compared to full crown preparation."},
            {"title": "Superior Strength", "desc": "Lithium disilicate withstands heavy chewing forces for years."},
            {"title": "Natural Appearance", "desc": "Translucent ceramic matches the natural tooth perfectly."},
            {"title": "Perfect Fit", "desc": "CAD/CAM technology ensures precise fit and optimal function."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "Inlay Procedure",
        "process_steps": [
            {"title": "1. Assessment & Preparation", "desc": "Decay removal and conservative tooth preparation."},
            {"title": "2. Digital Impression", "desc": "Precise digital scan for computer-aided design."},
            {"title": "3. CAD/CAM Fabrication", "desc": "Custom-milled from a single block of E-max ceramic."},
            {"title": "4. Adhesive Cementation", "desc": "Precision bonding for a seamless, permanent restoration."},
        ],
        "before_after": [
            {"before": "../before-after/E-max-inlay01.jpg", "after": "../before-after/E-max-inlay-after.jpg", "label": "E-Max Inlay Restoration"},
        ],
        "faqs": [
            {"q": "What is the advantage of an inlay over a filling?", "a": "Inlays are fabricated in a lab for superior strength, fit, and longevity. They last much longer than composite fillings and are more resistant to wear."},
            {"q": "Is the procedure painful?", "a": "The procedure is performed under local anesthesia and is completely painless. Most patients experience no discomfort during or after."},
            {"q": "How long do E-max inlays last?", "a": "With proper oral care, E-max inlays can last 15-20 years, significantly outlasting traditional composite fillings."},
        ],
        "sidebar_time": "45–60 minutes",
        "sidebar_visits": "2 Visits",
        "sidebar_anesthesia": "Painless Local",
        "sidebar_recovery": "Immediate",
        "sidebar_longevity": "15–20 Years",
        "doctor": {"name": "Dr. Sudhir Yadav", "title": "Prosthodontic Specialist", "img": "../doctor-sudhir-yadav.jpg", "desc": "Expert in precision ceramic restorations using advanced CAD/CAM technology."},
        "related": [
            {"name": "E-Max Crown", "href": "e-max-crown.html"},
            {"name": "E-Max Endocrown", "href": "e-max-endocrown.html"},
            {"name": "Root Canal Treatment", "href": "root-canal.html"},
        ],
        "cta_label": "Precision Ceramic Restorations",
        "cta_title": "Need a Precise, Durable<br>Tooth Restoration?",
        "cta_text": "Discover E-max inlays — the minimally invasive solution that preserves your tooth while restoring full strength and beauty.",
        "cta_btn_text": "Book Inlay Consultation →",
        "hero_img": "../before-after/E-max-inlay-after.jpg",
        "category": "implants",
    },
    {
        "slug": "laser-dentistry",
        "title": "Lasers for Gums Treatment",
        "page_title": "Laser Gum Treatment in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Advanced laser gum treatment in Gurgaon. Pain-free, no-stitch laser therapy for gum disease, gingivitis, and periodontal care.",
        "breadcrumb": "Laser Gum Treatment",
        "hero_label": "Advanced Laser Therapy",
        "hero_title": "Lasers for Gums<br>Treatment",
        "hero_subtitle": "A minimally invasive gum treatment using targeted laser energy to remove diseased tissue, eliminate bacteria, and promote rapid natural healing without scalpels or stitches.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20a%20Laser%20Gum%20Treatment%20consultation.",
        "overview_label": "Periodontal Care",
        "overview_title": "What Is Laser Gum Treatment?",
        "overview_text": "Laser Gum Treatment is a modern, non-invasive alternative to traditional gum surgery designed to treat gum disease, gingivitis, and aesthetic gum unevenness. By utilizing highly focused light energy, the laser precisely targets and removes infected gum tissue while sterilizing the underlying area and killing deep-seated bacteria. Because it cauterizes tissue and blood vessels simultaneously, laser therapy offers maximum precision with virtually no pain, minimal bleeding, and significantly faster healing times than conventional surgical methods.",
        "options_label": "Treatments",
        "options_title": "Laser Procedures",
        "options": [
            {"name": "Periodontal Laser Therapy", "desc": "Deep cleaning and sterilization of infected gum pockets."},
            {"name": "Laser Gum Contouring", "desc": "Reshaping gumline for aesthetic improvement and even margins."},
            {"name": "Laser Depigmentation", "desc": "Removal of dark spots on gums for a healthy pink appearance."},
            {"name": "Aphthous Ulcer Treatment", "desc": "Rapid pain relief and healing for mouth ulcers using laser."},
        ],
        "benefits_label": "Advantages",
        "benefits_title": "Why Choose Laser Treatment?",
        "benefits": [
            {"title": "Minimally Invasive", "desc": "Eliminates the need for traditional scalpels, cutting, or painful surgical incisions."},
            {"title": "No Stitches Required", "desc": "Cauterizes tissue instantly, eliminating the need for sutures."},
            {"title": "Virtually Painless", "desc": "Minimizes discomfort during and after the procedure while reducing bleeding and swelling."},
            {"title": "Faster Recovery", "desc": "Stimulates natural tissue regeneration, allowing patients to resume normal activities almost immediately."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "Laser Treatment Process",
        "process_steps": [
            {"title": "1. Diagnosis & Assessment", "desc": "Comprehensive periodontal examination and gum pocket depth measurement."},
            {"title": "2. Targeted Laser Application", "desc": "Laser fiber energy directed into gum pockets to vaporize infected tissue."},
            {"title": "3. Ultrasonic Cleaning", "desc": "Removing hardened plaque and tartar from root surfaces beneath the gumline."},
            {"title": "4. Tissue Sealing & Reattachment", "desc": "Secondary laser pass to seal the pocket and encourage natural gum reattachment."},
        ],
        "before_after": [],
        "faqs": [
            {"q": "Is laser gum treatment painful?", "a": "No. Laser gum treatment is virtually painless. Most patients require only minimal or no anesthesia and experience very little discomfort."},
            {"q": "How long is the recovery?", "a": "Recovery is significantly faster than traditional gum surgery. Most patients can resume normal activities the same day with minimal swelling."},
            {"q": "How many sessions are needed?", "a": "Most cases require 1-2 sessions depending on the severity of gum disease. Follow-up maintenance visits help maintain long-term gum health."},
        ],
        "sidebar_time": "30–60 minutes",
        "sidebar_visits": "1–2 Sessions",
        "sidebar_anesthesia": "Minimal/None",
        "sidebar_recovery": "Same Day",
        "sidebar_longevity": "Long-Term with Care",
        "doctor": {"name": "Dr. Sudhir Yadav", "title": "Laser Dentistry Specialist", "img": "../doctor-sudhir-yadav.jpg", "desc": "Expert in advanced laser periodontal therapy with state-of-the-art diode laser technology."},
        "related": [
            {"name": "General Dentistry", "href": "general-dentistry.html"},
            {"name": "Root Canal Treatment", "href": "root-canal.html"},
            {"name": "Dental Implants", "href": "dental-implants.html"},
        ],
        "cta_label": "Pain-Free Gum Treatment",
        "cta_title": "Concerned About Your<br>Gum Health?",
        "cta_text": "Experience the future of gum treatment with our advanced laser therapy. No scalpels, no stitches, no pain.",
        "cta_btn_text": "Book Laser Consultation →",
        "hero_img": "../treatments/Laser Dentistry.jpg",
        "category": "general",
    },
    {
        "slug": "dental-implant-bridge",
        "title": "Dental Implant Bridge",
        "page_title": "Dental Implant Bridge in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Permanent dental implant bridge in Gurgaon. Replace multiple missing teeth with implant-supported bridges for lasting stability and natural aesthetics.",
        "breadcrumb": "Dental Implant Bridge",
        "hero_label": "Fixed Implant Restorations",
        "hero_title": "Dental Implant Bridge<br>Treatment",
        "hero_subtitle": "A dental implant bridge is a permanent solution designed to replace several consecutive missing teeth using titanium dental implants for anchor support instead of natural teeth.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20a%20Dental%20Implant%20Bridge%20consultation.",
        "overview_label": "Implant Prosthodontics",
        "overview_title": "What Is a Dental Implant Bridge?",
        "overview_text": "A Dental Implant Bridge is an advanced restorative option designed to replace three or more missing teeth in a row. Unlike a traditional dental bridge—which requires shaving down adjacent healthy teeth—an implant bridge uses titanium implant posts anchored directly into the jawbone to secure the bridge. This structure restores full chewing capability, prevents bone loss, preserves natural facial symmetry, and provides a seamless, natural aesthetic without affecting neighboring healthy teeth.",
        "options_label": "Features",
        "options_title": "Key Advantages",
        "options": [
            {"name": "Preserves Natural Teeth", "desc": "No need to trim or alter adjacent healthy teeth for support."},
            {"name": "Prevents Bone Loss", "desc": "Implant posts stimulate the jawbone to maintain density."},
            {"name": "Exceptional Stability", "desc": "Securely anchored — no slippage or discomfort like dentures."},
            {"name": "Natural Appearance", "desc": "Custom-crafted to blend seamlessly with surrounding teeth."},
        ],
        "benefits_label": "Benefits",
        "benefits_title": "Why Choose an Implant Bridge?",
        "benefits": [
            {"title": "Preserves Natural Tooth Structure", "desc": "Eliminates the need to trim or alter adjacent healthy teeth for support."},
            {"title": "Prevents Bone Loss", "desc": "Implant posts stimulate the jawbone to maintain density and prevent facial sagging."},
            {"title": "Long-Term Durability", "desc": "Made from high-strength porcelain or ceramic materials designed for decades of use."},
            {"title": "Comfort & Stability", "desc": "Securely anchored in place, eliminating slippage or discomfort of removable dentures."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "Implant Bridge Process",
        "process_steps": [
            {"title": "1. Evaluation & Digital Planning", "desc": "Comprehensive oral assessment, 3D CBCT scanning, and digital placement planning."},
            {"title": "2. Implant Placement", "desc": "Surgical placement of titanium implant posts into the jawbone as anchor points."},
            {"title": "3. Healing & Osseointegration", "desc": "Healing period allowing the implants to fuse with surrounding bone tissue."},
            {"title": "4. Final Bridge Attachment", "desc": "Custom-made bridge secured onto the implants for a permanent restored smile."},
        ],
        "before_after": [
            {"before": "../before-after/Dental-implants-Bridge01.jpg", "after": "../before-after/Dental-implants-Bridge-after.jpg", "label": "Dental Implant Bridge"},
        ],
        "faqs": [
            {"q": "How many implants are needed for a bridge?", "a": "Typically 2 implant posts are needed to support a bridge replacing 3-4 missing teeth. Larger spans may require additional implants."},
            {"q": "Is implant bridge surgery painful?", "a": "No. The surgery is performed under local anesthesia and is pain-free. Most patients report mild discomfort for 1-2 days after, manageable with over-the-counter medication."},
            {"q": "How long does the entire process take?", "a": "The complete process takes 3-6 months, including the healing/osseointegration period. You'll have a temporary bridge during the healing phase."},
        ],
        "sidebar_time": "60–90 min (surgery)",
        "sidebar_visits": "3–4 Visits Total",
        "sidebar_anesthesia": "Painless Local",
        "sidebar_recovery": "3–6 Months (Total)",
        "sidebar_longevity": "20+ Years",
        "doctor": {"name": "Dr. Sudhir Yadav", "title": "Chief Implantologist & Surgeon", "img": "../doctor-sudhir-yadav.jpg", "desc": "Practising since 1998 with thousands of successful surgical implant bridge placements."},
        "related": [
            {"name": "Dental Implants", "href": "dental-implants.html"},
            {"name": "E-Max Ceramic Crowns", "href": "e-max-crown.html"},
            {"name": "Anterior PFM Bridge", "href": "anterior-pfm-bridge.html"},
        ],
        "cta_label": "Replace Multiple Missing Teeth",
        "cta_title": "Missing Several Teeth?<br>Get a Permanent Solution",
        "cta_text": "Schedule your implant bridge consultation today and restore your complete smile with fixed, permanent restorations.",
        "cta_btn_text": "Book Implant Bridge Consultation →",
        "hero_img": "../before-after/Dental-implants-Bridge-after.jpg",
        "category": "implants",
    },
    {
        "slug": "e-max-crown",
        "title": "E-Max Crown",
        "page_title": "E-Max Crown in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Premium E-Max all-ceramic crowns in Gurgaon. Metal-free lithium disilicate restorations with unmatched natural translucency and strength.",
        "breadcrumb": "E-Max Crown",
        "hero_label": "Premium All-Ceramic Restoration",
        "hero_title": "E-Max Ceramic Crown<br>Treatment",
        "hero_subtitle": "An E-max crown is a premium, metal-free lithium disilicate ceramic restoration that delivers superior translucency, unmatched lifelike aesthetics, and durable strength for damaged or discolored teeth.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20an%20E-Max%20Crown%20consultation.",
        "overview_label": "All-Ceramic Technology",
        "overview_title": "What Is an E-Max Crown?",
        "overview_text": "An E-max (Lithium Disilicate) Crown is a state-of-the-art, all-ceramic restoration engineered for ultimate strength and natural translucency. Unlike traditional metal-based crowns, E-max crowns blend seamlessly with your natural enamel, reflecting light in the exact same way. They are an ideal solution for restoring fractured, severely decayed, or heavily stained teeth—particularly in visible areas of your smile—without compromising on structural durability.",
        "options_label": "Features",
        "options_title": "E-Max Crown Features",
        "options": [
            {"name": "100% Metal-Free", "desc": "No dark lines at the gumline — pure ceramic beauty."},
            {"name": "Natural Translucency", "desc": "Reflects light like natural enamel for lifelike appearance."},
            {"name": "Superior Strength", "desc": "High-strength lithium disilicate resists chips and fractures."},
            {"name": "Biocompatible", "desc": "Gentle on gums and adjacent teeth — no allergic reactions."},
        ],
        "benefits_label": "Benefits",
        "benefits_title": "Why Choose E-Max Crowns?",
        "benefits": [
            {"title": "Exceptional Natural Aesthetics", "desc": "High translucency matches natural teeth for an invisible restoration."},
            {"title": "100% Metal-Free", "desc": "No dark lines or discoloration at the gumline — pure ceramic beauty."},
            {"title": "Superior Strength", "desc": "Chip and fracture resistant compared to conventional porcelain crowns."},
            {"title": "Biocompatible Material", "desc": "Gentle on adjacent natural teeth and gum tissue with no allergic risks."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "E-Max Crown Procedure",
        "process_steps": [
            {"title": "1. Smile Assessment", "desc": "Comprehensive evaluation, shade matching, and digital impression taking."},
            {"title": "2. Minimal Preparation", "desc": "Conservative tooth preparation to preserve maximum natural structure."},
            {"title": "3. Temporary Crown", "desc": "Temporary crown placed while the custom E-max crown is crafted."},
            {"title": "4. Precision Bonding", "desc": "Final shade verification and permanent bonding of the E-max crown."},
        ],
        "before_after": [
            {"before": "../before-after/E-max-crown01.jpg", "after": "../before-after/E-max-crown-after.jpg", "label": "E-Max Crown"},
        ],
        "faqs": [
            {"q": "How long do E-max crowns last?", "a": "With proper oral care, E-max crowns typically last 15-20 years. Their high-strength lithium disilicate construction ensures exceptional durability."},
            {"q": "Are E-max crowns better than PFM crowns?", "a": "E-max crowns offer superior aesthetics (no dark metal line), better biocompatibility, and excellent strength. They are ideal for front and back teeth."},
            {"q": "Can E-max crowns be used on back teeth?", "a": "Yes. E-max lithium disilicate is strong enough for posterior teeth while providing the natural translucency needed for front teeth."},
        ],
        "sidebar_time": "45–60 minutes",
        "sidebar_visits": "2 Visits (3 Days)",
        "sidebar_anesthesia": "Painless Local",
        "sidebar_recovery": "Immediate",
        "sidebar_longevity": "15–20 Years",
        "doctor": {"name": "Dr. Sudhir Yadav", "title": "Prosthodontic Specialist", "img": "../doctor-sudhir-yadav.jpg", "desc": "Expert in all-ceramic restorations with thousands of successful E-max crown placements."},
        "related": [
            {"name": "E-Max Endocrown", "href": "e-max-endocrown.html"},
            {"name": "E-Max Inlay", "href": "e-max-inlay.html"},
            {"name": "Dental Crowns & Bridges", "href": "dental-crowns-bridges.html"},
        ],
        "cta_label": "Premium Ceramic Crowns",
        "cta_title": "Need a Natural-Looking<br>Dental Crown?",
        "cta_text": "Discover E-max — the gold standard in all-ceramic crowns. Unmatched beauty and strength for your restored smile.",
        "cta_btn_text": "Book E-Max Crown Consultation →",
        "hero_img": "../before-after/E-max-crown-after.jpg",
        "category": "implants",
    },
    {
        "slug": "anterior-pfm-bridge",
        "title": "Anterior PFM Bridge",
        "page_title": "Anterior PFM Bridge in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Expert anterior PFM bridge treatment in Gurgaon. Porcelain-fused-to-metal crowns to replace missing front teeth with strength and aesthetics.",
        "breadcrumb": "Anterior PFM Bridge",
        "hero_label": "Front Tooth Restoration",
        "hero_title": "Anterior PFM Bridge<br>Treatment",
        "hero_subtitle": "An anterior PFM bridge replaces missing front teeth by anchoring handcrafted porcelain-fused-to-metal crowns onto adjacent natural teeth for immediate strength and aesthetics.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20an%20Anterior%20PFM%20Bridge%20consultation.",
        "overview_label": "Fixed Prosthodontics",
        "overview_title": "What Is an Anterior PFM Bridge?",
        "overview_text": "An Anterior PFM (Porcelain-Fused-to-Metal) Bridge is a reliable restorative solution designed to fill gaps in your front smile without requiring implant surgery. This procedure connects artificial teeth (pontics) to adjacent natural supporting teeth (abutments) using a durable inner metal alloy sub-structure coated with tooth-colored porcelain. It offers an excellent combination of structural strength and visual naturalness for multi-tooth front restorations.",
        "options_label": "Features",
        "options_title": "Key Features",
        "options": [
            {"name": "Metal Alloy Core", "desc": "Strong internal metal framework for maximum structural support."},
            {"name": "Porcelain Exterior", "desc": "Tooth-colored porcelain coating for natural front tooth appearance."},
            {"name": "No Surgery Required", "desc": "Fixed bridge placed without implant surgery — uses adjacent teeth."},
            {"name": "Quick Restoration", "desc": "Complete smile restoration in just 2-3 visits."},
        ],
        "benefits_label": "Benefits",
        "benefits_title": "Why Choose a PFM Bridge?",
        "benefits": [
            {"title": "Immediate Smile Restoration", "desc": "Fill gaps in your front smile quickly without implant surgery."},
            {"title": "Excellent Strength", "desc": "Metal alloy core provides superior structural durability for biting."},
            {"title": "Natural Appearance", "desc": "Porcelain coating matches surrounding teeth for a natural look."},
            {"title": "Proven Reliability", "desc": "Decades of clinical success with PFM bridge restorations worldwide."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "PFM Bridge Procedure",
        "process_steps": [
            {"title": "1. Assessment & Planning", "desc": "Evaluation of adjacent supporting teeth and bite analysis."},
            {"title": "2. Tooth Preparation", "desc": "Abutment teeth shaped to accommodate the bridge framework."},
            {"title": "3. Custom Fabrication", "desc": "Metal framework and porcelain coating crafted in the dental lab."},
            {"title": "4. Final Cementation", "desc": "Precision fitting, shade matching, and permanent cementation."},
        ],
        "before_after": [
            {"before": "../before-after/Anterior-pfm-bridge01.jpg", "after": "../before-after/Anterior-pfm-bridge-after.jpg", "label": "Anterior PFM Bridge"},
        ],
        "faqs": [
            {"q": "How long does a PFM bridge last?", "a": "With proper care, a PFM bridge typically lasts 10-15 years. Good oral hygiene and regular dental visits help extend its lifespan."},
            {"q": "Is a PFM bridge or implant better?", "a": "Both are excellent options. A PFM bridge is faster and doesn't require surgery, while an implant preserves bone and doesn't require altering adjacent teeth."},
            {"q": "Can I eat normally with a PFM bridge?", "a": "Yes. A PFM bridge restores full biting and chewing function. Avoid very hard foods like ice or hard candies to protect the porcelain coating."},
        ],
        "sidebar_time": "45–60 min per visit",
        "sidebar_visits": "2–3 Visits",
        "sidebar_anesthesia": "Painless Local",
        "sidebar_recovery": "Immediate",
        "sidebar_longevity": "10–15 Years",
        "doctor": {"name": "Dr. Sudhir Yadav", "title": "Prosthodontic Specialist", "img": "../doctor-sudhir-yadav.jpg", "desc": "Expert in fixed bridge restorations with extensive experience in anterior smile reconstruction."},
        "related": [
            {"name": "Dental Implant Bridge", "href": "dental-implant-bridge.html"},
            {"name": "E-Max Crown", "href": "e-max-crown.html"},
            {"name": "Dental Crowns & Bridges", "href": "dental-crowns-bridges.html"},
        ],
        "cta_label": "Restore Your Front Smile",
        "cta_title": "Missing Front Teeth?<br>Get a Seamless Bridge",
        "cta_text": "Schedule your PFM bridge consultation today and restore your front smile with a durable, natural-looking bridge.",
        "cta_btn_text": "Book Bridge Consultation →",
        "hero_img": "../before-after/Anterior-pfm-bridge-after.jpg",
        "category": "implants",
    },
    {
        "slug": "anterior-implant",
        "title": "Anterior Implant",
        "page_title": "Anterior Implant in Gurgaon — Muskan Dental & Implant Centre",
        "meta_desc": "Expert anterior dental implant in Gurgaon. Replace missing front teeth with a flawless, natural-looking titanium implant and ceramic crown.",
        "breadcrumb": "Anterior Implant",
        "hero_label": "Front Tooth Implant",
        "hero_title": "Anterior Dental<br>Implant",
        "hero_subtitle": "An anterior implant replaces missing front teeth, flawlessly restoring your smile aesthetics, speech clarity, and biting function.",
        "wa_text": "Hi%2C%20I%20would%20like%20to%20book%20an%20Anterior%20Implant%20consultation.",
        "overview_label": "Implant Dentistry",
        "overview_title": "What Is an Anterior Implant?",
        "overview_text": "Anterior teeth (your front incisors and canines) are the focal point of your smile. An anterior dental implant involves placing a high-grade titanium post into the jawbone to replace the root of a missing front tooth, capped with a custom-matched porcelain crown. Designed to blend imperceptibly with surrounding natural teeth, this treatment preserves your facial contours and prevents jawbone degradation.",
        "options_label": "Features",
        "options_title": "Key Features",
        "options": [
            {"name": "Premium Titanium Post", "desc": "High-grade titanium for lifetime integration with your jawbone."},
            {"name": "Custom Ceramic Crown", "desc": "Color and shape matched to surrounding natural teeth."},
            {"name": "Immediate Aesthetics", "desc": "Temporary crown placed on the day of surgery for instant smile."},
            {"name": "Preserves Facial Contours", "desc": "Prevents bone loss and maintains natural facial structure."},
        ],
        "benefits_label": "Benefits",
        "benefits_title": "Why Choose an Anterior Implant?",
        "benefits": [
            {"title": "Flawless Aesthetics", "desc": "Custom-matched crown blends imperceptibly with your natural front teeth."},
            {"title": "Restores Speech Clarity", "desc": "Front teeth are essential for proper speech — implant restores full clarity."},
            {"title": "Prevents Bone Loss", "desc": "Titanium post stimulates jawbone to maintain density and facial contours."},
            {"title": "Lifetime Solution", "desc": "Permanent replacement that functions and feels like your natural tooth."},
        ],
        "process_label": "Treatment Journey",
        "process_title": "Anterior Implant Process",
        "process_steps": [
            {"title": "1. 3D Scan & Planning", "desc": "CBCT scan and digital smile design for precise implant positioning."},
            {"title": "2. Implant Placement", "desc": "Titanium post placed with immediate temporary crown for aesthetics."},
            {"title": "3. Healing & Integration", "desc": "3-4 month osseointegration period as implant fuses with bone."},
            {"title": "4. Permanent Crown", "desc": "Custom ceramic crown permanently attached for a flawless smile."},
        ],
        "before_after": [
            {"before": "../before-after/anterior-implant01.jpg", "after": "../before-after/anterior-implant-after.jpg", "label": "Anterior Dental Implant"},
        ],
        "faqs": [
            {"q": "Can you see the implant from outside?", "a": "No. The ceramic crown is custom-matched to your natural teeth in color, shape, and size. It is virtually indistinguishable from a real tooth."},
            {"q": "How long does an anterior implant take?", "a": "The entire process takes 3-6 months including healing. A temporary crown is placed on the day of surgery so you're never without a front tooth."},
            {"q": "Is front tooth implant surgery painful?", "a": "No. The surgery is performed under local anesthesia and is pain-free. Most patients report less discomfort than a routine tooth extraction."},
        ],
        "sidebar_time": "30–45 minutes (surgery)",
        "sidebar_visits": "3 Visits Total",
        "sidebar_anesthesia": "Painless Local",
        "sidebar_recovery": "3–6 Months (Total)",
        "sidebar_longevity": "Lifetime Durability",
        "doctor": {"name": "Dr. Sudhir Yadav", "title": "Chief Implantologist & Surgeon", "img": "../doctor-sudhir-yadav.jpg", "desc": "Practising since 1998 specializing in aesthetic anterior implant placements."},
        "related": [
            {"name": "Dental Implants", "href": "dental-implants.html"},
            {"name": "Dental Implant Bridge", "href": "dental-implant-bridge.html"},
            {"name": "E-Max Crown", "href": "e-max-crown.html"},
        ],
        "cta_label": "Restore Your Front Smile",
        "cta_title": "Missing a Front Tooth?<br>Get a Perfect Replacement",
        "cta_text": "Book your anterior implant consultation today. Our implant experts will design a restoration that looks and feels completely natural.",
        "cta_btn_text": "Book Anterior Implant Consultation →",
        "hero_img": "../before-after/anterior-implant-after.jpg",
        "category": "implants",
    },
]


def generate_treatment_html(t):
    """Generate the complete HTML for a treatment page."""
    
    # Build before-after section
    ba_html = ""
    if t["before_after"]:
        ba_cards = ""
        for ba in t["before_after"]:
            ba_cards += f"""
              <div class="ba-card">
                <div class="ba-card__images">
                  <div class="ba-card__side">
                    <span class="ba-card__label">Before</span>
                    <img src="{ba['before']}" alt="Before {t['title']} Treatment" loading="lazy">
                  </div>
                  <div class="ba-card__divider"></div>
                  <div class="ba-card__arrow">→</div>
                  <div class="ba-card__side">
                    <span class="ba-card__label">After</span>
                    <img src="{ba['after']}" alt="After {t['title']} Treatment" loading="lazy">
                  </div>
                </div>
                <div class="ba-card__info">
                  <span class="ba-card__treatment">{ba['label']}</span>
                </div>
              </div>"""
        
        ba_html = f"""
          <!-- Before & After Results -->
          <div class="reveal" style="margin-bottom: var(--space-8);">
            <span class="section__label" style="text-align: left;">Clinical Results</span>
            <h2 style="font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-navy); margin-bottom: var(--space-3);">Before & After</h2>
            <p style="font-size: 0.95rem; color: var(--color-gray-600); line-height: 1.6; margin-bottom: var(--space-4);">Real patient {t['title'].lower()} transformation at Muskan Dental.</p>

            <div class="ba-grid" style="max-width: 520px;">{ba_cards}
            </div>

            <div style="margin-top: var(--space-4);">
              <a href="../gallery.html" class="btn btn--outline btn--sm" style="font-size: 0.85rem;">View Full Gallery →</a>
            </div>
          </div>
"""

    # Build options grid
    options_html = ""
    for opt in t["options"]:
        options_html += f"""
              <div style="background: var(--color-gray-50); padding: 18px; border-radius: 10px; border-left: 3px solid var(--color-primary);">
                <h4 style="font-family: var(--font-heading); font-size: 1.05rem; color: var(--color-navy); margin-bottom: 4px;">{opt['name']}</h4>
                <p style="font-size: 0.85rem; color: var(--color-gray-600); line-height: 1.5; margin: 0;">{opt['desc']}</p>
              </div>"""

    # Build benefits
    benefits_html = ""
    for i, b in enumerate(t["benefits"], 1):
        benefits_html += f"""
              <div class="benefit-item">
                <div class="benefit-item__number">{i}</div>
                <div class="benefit-item__text">
                  <h4>{b['title']}</h4>
                  <p>{b['desc']}</p>
                </div>
              </div>"""

    # Build timeline
    steps_html = ""
    for i, s in enumerate(t["process_steps"]):
        is_last = i == len(t["process_steps"]) - 1
        color = "var(--color-gold)" if is_last else "var(--color-primary)"
        mb = "" if is_last else " margin-bottom: 20px;"
        steps_html += f"""
              <div style="position: relative;{mb}">
                <div style="position: absolute; left: -37px; top: 0; width: 16px; height: 16px; border-radius: 50%; background: {color}; border: 3px solid var(--color-white); box-shadow: 0 0 0 2px {color};"></div>
                <h4 style="font-family: var(--font-heading); font-size: 1.05rem; color: var(--color-navy); margin-bottom: 4px;">{s['title']}</h4>
                <p style="font-size: 0.85rem; color: var(--color-gray-600); line-height: 1.5; margin: 0;">{s['desc']}</p>
              </div>
"""

    # Build FAQ
    faq_html = ""
    for faq in t["faqs"]:
        faq_html += f"""
              <div class="faq-item">
                <button class="faq-question">{faq['q']} <span class="faq-icon"></span></button>
                <div class="faq-answer">
                  <p>{faq['a']}</p>
                </div>
              </div>"""

    # Build related links
    related_html = ""
    for r in t.get("related", []):
        related_html += f"""
              <a href="{r['href']}" style="font-size: 0.88rem; color: var(--color-primary); text-decoration: none; font-weight: 500;">→ {r['name']}</a>"""

    doc = t.get("doctor", {})

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t['page_title']}</title>
  <meta name="description" content="{t['meta_desc']}">
  <link rel="stylesheet" href="../styles.css?v=9">
  <link rel="icon" href="../muskan-logo.png" type="image/png">
</head>
<body>

  <!-- ========== HEADER ========== -->
  <header class="header" id="header">
    <div class="container header__inner">
      <a href="../index.html" class="header__logo">
        <img src="../muskan-logo.png" alt="Muskan Dental" width="140">
      </a>
      <nav class="header__nav" id="mainNav">
        <a href="../index.html" class="header__nav-link">Home</a>
        <a href="../index.html#about" class="header__nav-link">About</a>
        <a href="../treatments.html" class="header__nav-link active">Treatments</a>
        <a href="../index.html#doctors" class="header__nav-link">Doctors</a>
        <a href="../international.html" class="header__nav-link">Dental Tourism</a>
        <a href="../gallery.html" class="header__nav-link">Gallery</a>
        <a href="../testimonials.html" class="header__nav-link">Our Patient Stories</a>
        <a href="../index.html#contact" class="header__nav-link">Contact</a>
      </nav>
      <a href="tel:+919810580837" class="header__phone">
        <span>📞</span> +91 98105 80837
      </a>
      <button class="header__hamburger" id="hamburger" aria-label="Menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
    <div class="header__mobile-nav" id="mobileNav">
      <a href="../index.html" data-mobile-link>Home</a>
      <a href="../index.html#about" data-mobile-link>About</a>
      <a href="../treatments.html" data-mobile-link>Treatments</a>
      <a href="../index.html#doctors" data-mobile-link>Doctors</a>
      <a href="../international.html" data-mobile-link>Dental Tourism</a>
      <a href="../gallery.html" data-mobile-link>Gallery</a>
      <a href="../testimonials.html" data-mobile-link>Our Patient Stories</a>
      <a href="../index.html#contact" data-mobile-link>Contact</a>
    </div>
  </header>

  <!-- ========== PAGE HERO ========== -->
  <section class="page-hero">
    <div class="page-hero__bg">
      <img src="{t['hero_img']}" alt="{t['title']} - Muskan Dental" loading="eager">
    </div>
    <div class="page-hero__overlay"></div>
    <div class="container">
      <div class="page-hero__content">
        <nav class="breadcrumbs">
          <a href="../index.html">Home</a>
          <span class="breadcrumbs__sep">›</span>
          <a href="../treatments.html">Treatments</a>
          <span class="breadcrumbs__sep">›</span>
          <span class="breadcrumbs__current">{t['breadcrumb']}</span>
        </nav>
        <span class="page-hero__label">{t['hero_label']}</span>
        <h1 class="page-hero__title">{t['hero_title']}</h1>
        <p class="page-hero__subtitle">{t['hero_subtitle']}</p>
        <div class="page-hero__actions">
          <a href="https://wa.me/919810580837?text={t['wa_text']}" target="_blank" rel="noopener" class="btn btn--primary">Book {t['title']} Consultation →</a>
          <a href="tel:+919810580837" class="btn btn--outline-white">Call +91 98105 80837</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ========== TREATMENT CONTENT & SIDEBAR ========== -->
  <section class="section">
    <div class="container">
      <div class="treatment-layout">
        
        <!-- Main Content -->
        <div class="treatment-content">
          
          <!-- Overview -->
          <div class="reveal" style="margin-bottom: var(--space-8);">
            <span class="section__label" style="text-align: left;">{t['overview_label']}</span>
            <h2 style="font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-navy); margin-bottom: var(--space-3);">{t['overview_title']}</h2>
            <p style="font-size: 0.95rem; color: var(--color-gray-600); line-height: 1.7; margin-bottom: var(--space-3);">{t['overview_text']}</p>
          </div>

          <!-- Options -->
          <div class="reveal" style="margin-bottom: var(--space-8);">
            <span class="section__label" style="text-align: left;">{t['options_label']}</span>
            <h2 style="font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-navy); margin-bottom: var(--space-3);">{t['options_title']}</h2>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px;">{options_html}
            </div>
          </div>

          <!-- Benefits -->
          <div class="reveal" style="margin-bottom: var(--space-8);">
            <span class="section__label" style="text-align: left;">{t['benefits_label']}</span>
            <h2 style="font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-navy); margin-bottom: var(--space-3);">{t['benefits_title']}</h2>
            
            <div class="benefit-list">{benefits_html}
            </div>
          </div>

          <!-- Step by Step Timeline -->
          <div class="reveal" style="margin-bottom: var(--space-8);">
            <span class="section__label" style="text-align: left;">{t['process_label']}</span>
            <h2 style="font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-navy); margin-bottom: var(--space-3);">{t['process_title']}</h2>
            
            <div class="timeline" style="position: relative; padding-left: 28px; border-left: 2px solid var(--color-gray-200); margin-top: 18px;">{steps_html}
            </div>
          </div>
{ba_html}
          <!-- FAQ Accordion -->
          <div class="reveal" style="margin-bottom: var(--space-8);">
            <span class="section__label" style="text-align: left;">Frequently Asked Questions</span>
            <h2 style="font-family: var(--font-heading); font-size: 1.85rem; font-weight: 700; color: var(--color-navy); margin-bottom: var(--space-3);">{t['title']} FAQ</h2>
            
            <div class="faq-list">{faq_html}
            </div>
          </div>

        </div>

        <!-- Sticky Sidebar -->
        <aside class="treatment-sidebar">
          
          <!-- Treatment Quick Facts -->
          <div class="treatment-sidebar__card reveal">
            <h3 style="font-family: var(--font-heading); font-size: 1.25rem; color: var(--color-navy); margin-bottom: 16px; border-bottom: 2px solid var(--color-primary-subtle); padding-bottom: 10px;">Treatment Overview</h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
              <li style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid var(--color-gray-100); font-size: 0.9rem;">
                <span style="color: var(--color-gray-500);">Procedure Time:</span>
                <strong style="color: var(--color-navy);">{t['sidebar_time']}</strong>
              </li>
              <li style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid var(--color-gray-100); font-size: 0.9rem;">
                <span style="color: var(--color-gray-500);">Visits:</span>
                <strong style="color: var(--color-navy);">{t['sidebar_visits']}</strong>
              </li>
              <li style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid var(--color-gray-100); font-size: 0.9rem;">
                <span style="color: var(--color-gray-500);">Anesthesia:</span>
                <strong style="color: var(--color-navy);">{t['sidebar_anesthesia']}</strong>
              </li>
              <li style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid var(--color-gray-100); font-size: 0.9rem;">
                <span style="color: var(--color-gray-500);">Recovery:</span>
                <strong style="color: var(--color-navy);">{t['sidebar_recovery']}</strong>
              </li>
              <li style="display: flex; justify-content: space-between; padding: 10px 0; font-size: 0.9rem;">
                <span style="color: var(--color-gray-500);">Longevity:</span>
                <strong style="color: var(--color-gold);">{t['sidebar_longevity']}</strong>
              </li>
            </ul>
          </div>

          <!-- Doctor Specialist Card -->
          <div class="treatment-sidebar__card reveal" style="text-align: center;">
            <img src="{doc['img']}" alt="{doc['name']}" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; margin: 0 auto 12px; border: 3px solid var(--color-gold);">
            <h4 style="font-family: var(--font-heading); font-size: 1.15rem; color: var(--color-navy); margin-bottom: 4px;">{doc['name']}</h4>
            <p style="font-size: 0.8rem; color: var(--color-primary); font-weight: 600; margin-bottom: 12px;">{doc['title']}</p>
            <p style="font-size: 0.85rem; color: var(--color-gray-600); line-height: 1.5; margin-bottom: 16px;">{doc['desc']}</p>
            <a href="https://wa.me/919810580837?text=Hi%20Dr.%20Muskan,%20I%20would%20like%20to%20consult%20regarding%20{t['title'].replace(' ', '%20')}." target="_blank" rel="noopener" class="btn btn--primary" style="width: 100%; padding: 10px;">Consult with Specialist</a>
          </div>

          <!-- Related Treatments -->
          <div class="treatment-sidebar__card reveal">
            <h4 style="font-family: var(--font-heading); font-size: 1.1rem; color: var(--color-navy); margin-bottom: 12px;">Related Treatments</h4>
            <div style="display: flex; flex-direction: column; gap: 8px;">{related_html}
            </div>
          </div>

        </aside>

      </div>
    </div>
  </section>

  <!-- ========== CALL TO ACTION ========== -->
  <section class="cta-section">
    <div class="container">
      <div class="cta-card reveal">
        <div class="cta-card__bg">
          <img src="../bg/cta-bg.png" alt="Luxury dental clinic interior" loading="lazy">
        </div>
        <div class="cta-card__overlay"></div>
        <div class="cta-card__content">
          <div class="cta-card__text">
            <span class="section__label" style="color: var(--color-gold);">{t['cta_label']}</span>
            <h2 class="cta-card__title">{t['cta_title']}</h2>
            <p class="cta-card__subtitle">{t['cta_text']}</p>
          </div>
          <div class="cta-card__actions">
            <a href="https://wa.me/919810580837?text={t['wa_text']}" target="_blank" rel="noopener" class="btn btn--gold btn--lg">{t['cta_btn_text']}</a>
            <a href="tel:+919810580837" class="btn btn--outline-white btn--lg">Call +91 98105 80837</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========== FOOTER ========== -->
  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <img src="../muskan-logo.png" alt="Muskan Dental Logo" class="footer__logo">
          <p class="footer__desc">Muskan Dental & Implant Centre is a leading luxury dental clinic in Gurgaon, practising since 1998 and providing advanced implantology, cosmetic smile makeovers, and specialized oral care.</p>
        </div>
        <div class="footer__links">
          <h4 class="footer__title">Quick Links</h4>
          <ul>
            <li><a href="../index.html">Home</a></li>
            <li><a href="../index.html#about">About Us</a></li>
            <li><a href="../treatments.html">Treatments</a></li>
            <li><a href="../index.html#doctors">Our Doctors</a></li>
            <li><a href="../international.html">Dental Tourism</a></li>
            <li><a href="../gallery.html">Gallery</a></li>
            <li><a href="../testimonials.html">Our Patient Stories</a></li>
          </ul>
        </div>
        <div class="footer__links">
          <h4 class="footer__title">Treatments</h4>
          <ul>
            <li><a href="dental-implants.html">Dental Implants</a></li>
            <li><a href="veneers.html">Porcelain Veneers</a></li>
            <li><a href="e-max-crown.html">E-Max Porcelain Crowns</a></li>
            <li><a href="smile-makeover.html">Smile Makeover</a></li>
            <li><a href="root-canal.html">Root Canal Treatment</a></li>
            <li><a href="orthodontics.html">Orthodontics & Aligners</a></li>
            <li><a href="../treatments.html" style="color: var(--color-primary); font-weight: 600;">All 18 Treatments →</a></li>
          </ul>
        </div>
        <div class="footer__contact">
          <h4 class="footer__title">Contact Us</h4>
          <p>📍 Sector 15 & Friends Colony, Gurgaon, HR</p>
          <p>📞 <a href="tel:+919810580837" style="color: inherit;">+91 98105 80837</a></p>
          <p>✉️ <a href="mailto:info@muskandental.com" style="color: inherit;">info@muskandental.com</a></p>
          <p>⏰ Mon - Sat: 10:00 AM - 8:00 PM</p>
        </div>
      </div>
      <div class="footer__bottom">
        <p>&copy; 2026 Muskan Dental & Implant Centre. All Rights Reserved.</p>
      </div>
    </div>
  </footer>

  <script src="../script.js?v=2"></script>
</body>
</html>
"""
    return html


# Generate all treatment pages
if __name__ == "__main__":
    for t in treatments:
        filepath = os.path.join(TREATMENTS_DIR, f"{t['slug']}.html")
        html = generate_treatment_html(t)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {t['slug']}.html")

print(f"\nAll {len(treatments)} treatment pages generated successfully!")
