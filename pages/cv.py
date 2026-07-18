import streamlit as st
import utils.ui as ui

left, center, right =st.columns(3)
with center:
    st.title("Louka Abed")

left, center, right =st.columns(3)
with left:
    st.write("Malden, MA 02148")
with center:
    st.write("\tPhone: 617-942-1441")
with right:
    st.write("E-Mail: contact@loukaabed.com")
st.subheader("Clinical Data Scientist | AI Translational Medicine & Pharma R&D", divider="green", anchor=False)
st.write("""International Medical Graduate (MD) combining clinical and biochemistry domain expertise with MS in Data Science and Mathematics foundations to validate, 
audit, model, and extract AI insights—accelerating novel drug discovery and building predictive translational medicine pipelines through a systems approach 
that integrates complex healthcare data streams, high-throughput genomic and proteomic registries, and heterogeneous multiomics architectures.""")

st.info("Employment Status:** US Citizen | Fully authorized for US employment with no sponsorship required.")

st.divider()

st.header("Education", divider="green", anchor=False)
st.write("""
* **MS in Data Science** | Eastern University
    - **Completed Coursework:** Principles of Python Programming...
""")

st.html("<h3><b>Bachelor of Medicine and Surgery (M.B. B.Ch.)</b></h3>") 
st.html("<h4><b>Cairo University Faculty of Medicine</b>Equivalent to MD in the US</b></h4>")
st.html("<blockquote><b>Clerkship:</b> Emergency Medicine, ENT, Forensic Medicine</blockquote>")


st.write("Doctor of Medicine")
st.write("Columbia University College of Physicians and Surgeons, New York")
st.write("Successfully completed clinical clerkships in medicine, pediatrics, obstetrics & gynecology, psychiatry, surgery, routinely used Electronic Health Record (EHR). Passed US Medical Licensing Exam step 1 (USMLE step 1).")

st.write("Bachelor of Science in Biochemistry & Mathematics Minor")
st.write("University of Massachusetts (UMass), Boston")
st.write("Summa Cum Laude graduate with Honors in Biochemistry, top of my class, GPA 3.86/4.00")

st.divider()

st.subheader("Work History")

st.write("Manufacturing Associate — GMP Manufacturing - Moderna — Burlington, MA — 04/2023 – 03/2025")
st.write("• Working in the personalized cancer vaccine (PCV) unit")
st.write("• Routinely used SOP, GMP, aseptic technique, SAP, Syncade, Biosafety Cabinet (BSC), chromatography, Sequencher")

st.write("Family Medicine Resident Physician — Ministry of Health — Port Said, Egypt — 03/2021 – 02/2023")
st.write("• Rotation through primary care clinic, pediatrics, internal Medicine, and emergency medicine")

st.write("Medical Internship — Cairo University Teaching Hospitals — Cairo, Egypt — 03/2019 – 04/2020")
st.write("• One year of clinical clerkships required to be a licensed physician in Egypt.")

st.write("Medical Data Analyst — Innodata – Synodex Division — Hackensack, NJ")
st.write("• Literature review to create up-to-date evidence-based medical risk elements in order to accurately predict the real liability in disability & life insurance")
st.write("• Advanced skills in Excel (VB macros, searching, sorting, matching, text extraction/editing)")

st.write("Research Associate — Columbia University Medical Center - Systems Biology — NY")
st.write("• Predicting computationally cellular response (i.e., Gene Expression) to drug combinations (inspired by Connectivity Map)")
st.write("• Designed experiment, wrote protocol, ordered lab supplies & drugs, initiated cell culture, propagated, maintained & cryopreserved stock of mammalian immortal cells (MCF7), cell counting, aseptic/sterile technique")
st.write("• In vitro drug testing, determined the optimum drug dosage for maximum mRNA cellular response, isolation & quantification mRNA via spectrophotometry, sent mRNA for gene sequencing.")

st.write("Research Associate (Summer) — Columbia University Medical Center, Nephrology Division — NY")
st.write("• Role of Copy-Number Variations (CNVs) in vesicoureteric reflux (VUR) in children of Ashkenazi Jewish families")
st.write("• Used Real-Time qPCR (qRT-PCR) to validate & quantify the presence of rare CNVs")
st.write("• Used online resources extensively: UCSC genome browser, dbSNP, Primer3, primer design")

st.write("Process Development Associate (Contract) — Broad Institute — Cambridge, MA")
st.write("• Sequencing gaps and diﬀicult-to-sequence regions in genomes of diﬀerent microorganisms using Primer Walking")
st.write("• Operating Multiprobe robot for automatic liquid reagents dispensing (High Throughput Technique)")
st.write("• Routinely used 96-wells, made labels, barcode plate reader, thermal plate sealer")

st.write("Research Assistant (Summer) — Beth Israel Deaconess Medical Center - The Division of Matrix Biology — Boston, MA")
st.write("• Role of carcinoma-associated fibroblasts in breast cancer: local recruit vs distant BM in-vivo mouse study")
st.write("• Gained skills in tissue genotyping, tumor cell culture (4T1), fibroblasts primary cell culture, paraﬀin embedding & sectioning using microtome, Immunohistochemistry (IHC) & Immunofluorescence (IF) staining, H&E staining")

st.write("Research Assistant (Work-study) — University of Massachusetts, Department of Biology — Boston, MA")
st.write("• Study of cell signaling in-vivo Drosophila, applying post-transcriptional gene silencing using RNAi vector")
st.write("• DNA cloning / subcloning, restriction enzymes digest, ligation, competent E. Coli, heat transformation")
st.write("• Streaking/plating agar, PCR colonies screening, plasmid extraction, miniprep, spectrophotometry")

st.divider()

st.subheader("Data Science skills")
st.write("• Programming in Python, Java, MATLAB, R, Microsoft Excel Macros")
st.write("• Coursework: calculus, linear algebra, differential equations, mathematical biology, probability & Statistics")

st.divider()

st.subheader("Accomplishments")
st.write("• Emil Fischer Book Award, Honors, and Distinction in Biochemistry: UMass Boston")
st.write("• Dean List: UMass Boston")
st.write("• Tutor Certificate of Recognition: Academic Support UMass Boston")
st.write("• Classroom Leadership Award: UMass Boston Honors Program")
st.write("• Ronald's McNair Post Baccalaureate Achievement Program Scholar")

st.divider()

st.subheader("Certifications")
st.write("• Certified General Medical Practitioner (Physician/MD) — Ministry of Health & Population, Egypt — 06/2020")
st.write("• Certified in Immediate Life Support (ILS) / Basic Life Support (BLS) — European Resuscitation Council")

st.divider()

st.subheader("Publications")
st.write('Phillip Kyriakakis; Marla Tipping; Louka Abed; Alexey Veraksa. "Tandem affinity purification in Drosophila: The advantages of the GS-TAP system." Fly Vol: 2:229-235. (Published under former name)')

st.divider()

ui.message()