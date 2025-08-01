from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random

class PersonalBrandingBot:
    def __init__(self, form_url):
        self.form_url = form_url
        self.driver = None
        
        # Data untuk variasi jawaban
        self.names = [
            "Ahmad Rizki", "Sari Wijayanti", "Budi Santoso", "Maya Sari", "Dimas Prakoso",
            "Indira Putri", "Eko Prasetyo", "Lina Maharani", "Fajar Nugroho", "Dewi Lestari",
            "Arif Rahman", "Putri Andini", "Yoga Pratama", "Nina Kusuma", "Bayu Wijaya"
        ]
        
        self.social_medias = [
            "Instagram: @ahmad_rizki", "LinkedIn: Sari Wijayanti", "Instagram: @budisantoso",
            "TikTok: @mayasari", "LinkedIn: Dimas Prakoso", "Instagram: @indiraputri",
            "LinkedIn: Eko Prasetyo", "Instagram: @linamaharani", "LinkedIn: Fajar Nugroho",
            "Instagram: @dewilestari", "LinkedIn: Arif Rahman", "Instagram: @putriandini",
            "LinkedIn: Yoga Pratama", "Instagram: @ninakusuma", "TikTok: @bayuwijaya"
        ]
        
        self.occupations = [
            "Mahasiswa Teknik Informatika", "Karyawan swasta di bidang IT", "Freelancer Graphic Designer",
            "Mahasiswa Ekonomi", "Marketing Executive", "Content Creator", "Data Analyst",
            "Mahasiswa Psikologi", "HR Specialist", "Social Media Manager", "UI/UX Designer",
            "Mahasiswa Komunikasi", "Digital Marketing Specialist", "Business Analyst", "Entrepreneur"
        ]
        
        # Template jawaban untuk pertanyaan essay
        self.important_things = [
            "Konsistensi adalah kunci utama dalam membangun personal branding yang kuat. Seseorang harus mampu mempertahankan pesan, nilai, dan citra yang sama di semua platform dan interaksi. Selain itu, keaslian (authenticity) juga sangat penting karena audiens dapat dengan mudah mendeteksi ketidakjujuran. Kemampuan storytelling yang baik juga diperlukan untuk menyampaikan nilai dan pengalaman dengan cara yang menarik dan relatable bagi target audiens.",
            
            "Keunikan atau unique selling point merupakan fondasi terpenting dalam personal branding. Seseorang harus mampu mengidentifikasi apa yang membedakannya dari orang lain dan mengkomunikasikan nilai tersebut dengan jelas. Networking yang strategis juga krusial karena personal branding bukan hanya tentang membangun citra, tetapi juga tentang membangun hubungan yang bermakna dengan orang-orang yang tepat dalam industri atau bidang yang diminati.",
            
            "Visi yang jelas tentang tujuan karier dan dampak yang ingin diciptakan adalah hal paling fundamental. Seseorang perlu memahami mengapa mereka ingin membangun personal branding dan apa yang ingin mereka capai. Selain itu, kemampuan adaptasi terhadap perubahan tren dan platform baru sangat penting karena dunia digital terus berkembang. Continuous learning dan self-improvement juga menjadi kunci untuk tetap relevan.",
            
            "Expertise atau keahlian yang mendalam di bidang tertentu adalah aset terbesar dalam personal branding. Seseorang harus terus mengasah kemampuan dan pengetahuannya agar dapat memberikan value yang nyata kepada audiensnya. Emotional intelligence juga penting untuk memahami dan berinteraksi dengan berbagai tipe audiens, serta kemampuan untuk menerima feedback dan kritik konstruktif untuk perbaikan berkelanjutan."
        ]
        
        self.social_media_roles = [
            "Media sosial berperan sebagai platform utama untuk membangun visibilitas dan engagement dengan audiens target. Melalui media sosial, seseorang dapat secara konsisten membagikan konten yang mencerminkan keahlian, nilai, dan kepribadiannya. Platform ini memungkinkan interaksi dua arah yang membantu membangun hubungan personal dengan followers. Media sosial juga berfungsi sebagai portfolio digital yang dapat diakses kapan saja oleh calon klien, employer, atau kolaborator.",
            
            "Media sosial berfungsi sebagai amplifier yang memperluas jangkauan personal branding seseorang. Dengan algoritma yang tepat dan konten yang berkualitas, seseorang dapat menjangkau audiens yang lebih luas dari yang mungkin dicapai melalui networking tradisional. Platform ini juga memungkinkan real-time feedback dari audiens, sehingga seseorang dapat terus menyesuaikan dan memperbaiki strategi branding-nya berdasarkan respons yang diterima.",
            
            "Peran media sosial dalam personal branding adalah sebagai storytelling platform yang memungkinkan seseorang untuk berbagi journey, pembelajaran, dan insight secara autentik. Media sosial memberikan kesempatan untuk menunjukkan behind-the-scenes dari kehidupan profesional, yang membuat personal branding terasa lebih human dan relatable. Platform ini juga berfungsi sebagai networking tool yang powerful untuk terhubung dengan industry leaders dan potential opportunities.",
            
            "Media sosial berperan sebagai measurement tool yang membantu seseorang memahami seberapa efektif personal branding yang dibangun. Melalui analytics dan engagement metrics, seseorang dapat mengevaluasi jenis konten apa yang paling resonan dengan audiensnya. Media sosial juga menjadi platform untuk thought leadership, di mana seseorang dapat memposisikan diri sebagai expert di bidangnya melalui konten edukatif dan insights yang valuable."
        ]
        
        self.authenticity_importance = [
            "Keaslian sangat penting karena merupakan fondasi kepercayaan dalam personal branding. Audiens saat ini sangat cerdas dalam mendeteksi ketidakjujuran atau persona yang dibuat-buat. Authenticity memungkinkan seseorang untuk membangun hubungan yang genuine dan sustainable dengan audiensnya. Ketika seseorang authentic, mereka akan menarik audiens yang benar-benar align dengan nilai dan visi mereka, sehingga menghasilkan engagement yang lebih bermakna dan loyal.",
            
            "Authenticity adalah kunci diferensiasi yang paling kuat dalam personal branding. Dalam dunia yang penuh dengan konten dan noise, keaslian membuat seseorang stand out dari kompetitor. Ketika seseorang konsisten menunjukkan kepribadian aslinya, mereka akan membangun emotional connection yang kuat dengan audiens. Hal ini juga mengurangi burden untuk 'menjaga karakter' karena seseorang hanya perlu menjadi diri sendiri secara konsisten.",
            
            "Keaslian sangat krusial karena mempengaruhi longevity dari personal branding seseorang. Personal branding yang dibangun berdasarkan authenticity akan lebih sustainable karena tidak memerlukan energi ekstra untuk mempertahankan persona palsu. Authenticity juga memungkinkan personal growth yang natural, di mana personal branding dapat berkembang seiring dengan perkembangan pribadi seseorang tanpa kehilangan core identity.",
            
            "Authenticity penting karena menciptakan trust dan credibility yang merupakan currency terpenting dalam personal branding. Ketika seseorang authentic, mereka akan lebih mudah mendapatkan referral, recommendation, dan opportunities karena orang-orang percaya pada integritas mereka. Keaslian juga memungkinkan seseorang untuk vulnerable dan sharing failures atau challenges, yang justru membuat personal branding lebih relatable dan inspiratif bagi audiens."
        ]
        
    def setup_driver(self):
        """Setup Chrome WebDriver"""
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # Uncomment next line to run headlessly
        # options.add_argument('--headless')
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        
    def generate_random_data(self):
        """Generate random form data"""
        return {
            'nama': random.choice(self.names),
            'sosial_media': random.choice(self.social_medias),
            'kesibukan': random.choice(self.occupations),
            'likert_scores': [random.randint(3, 5) for _ in range(14)],  # 14 pertanyaan likert
            'important_thing': random.choice(self.important_things),
            'social_media_role': random.choice(self.social_media_roles),
            'authenticity': random.choice(self.authenticity_importance)
        }
    
    # ...existing code...

    def fill_form(self, data):
        """Fill the Google Form with provided data"""
        try:
            self.driver.get(self.form_url)
            time.sleep(5)
            
            print("=== PAGE 1: Basic Info ===")
            
            # Fill Nama
            try:
                nama_field = WebDriverWait(self.driver, 15).until(
                    EC.any_of(
                        EC.presence_of_element_located((By.XPATH, "//input[contains(@aria-label, 'Nama')]")),
                        EC.presence_of_element_located((By.XPATH, "//input[@type='text'][1]")),
                        EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
                    )
                )
                nama_field.clear()
                nama_field.send_keys(data['nama'])
                print(f"✓ Filled nama: {data['nama']}")
                time.sleep(1)
            except Exception as e:
                print(f"❌ Error filling nama: {e}")
                return False
            
            # Fill Sosial Media
            try:
                sosmed_inputs = self.driver.find_elements(By.XPATH, "//input[@type='text']")
                if len(sosmed_inputs) >= 2:
                    sosmed_inputs[1].clear()
                    sosmed_inputs[1].send_keys(data['sosial_media'])
                    print(f"✓ Filled sosial media: {data['sosial_media']}")
                time.sleep(1)
            except Exception as e:
                print(f"❌ Error filling sosial media: {e}")
            
            # Fill Kesibukan
            try:
                kesibukan_inputs = self.driver.find_elements(By.XPATH, "//input[@type='text']")
                if len(kesibukan_inputs) >= 3:
                    kesibukan_inputs[2].clear()
                    kesibukan_inputs[2].send_keys(data['kesibukan'])
                    print(f"✓ Filled kesibukan: {data['kesibukan']}")
                time.sleep(1)
            except Exception as e:
                print(f"❌ Error filling kesibukan: {e}")
            
            # Click Next to go to PAGE 2
            try:
                next_button = WebDriverWait(self.driver, 10).until(
                    EC.any_of(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]/parent::*")),
                        EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/parent::*")),
                        EC.element_to_be_clickable((By.XPATH, "//div[@role='button'][contains(., 'Next')]"))
                    )
                )
                next_button.click()
                print("✓ Navigated to PAGE 2: Likert & Essay Questions")
                time.sleep(4)
            except Exception as e:
                print(f"❌ Error navigating to page 2: {e}")
                return False
            
            print("=== PAGE 2: Likert Scale Questions & Essay Questions ===")
            
            # Fill Likert scale questions
            print("Filling Likert scale questions...")
            for i, score in enumerate(data['likert_scores']):
                try:
                    time.sleep(1)
                    radio_groups = self.driver.find_elements(By.XPATH, "//div[@role='radiogroup']")
                    
                    if i < len(radio_groups):
                        radios_in_group = radio_groups[i].find_elements(By.XPATH, ".//div[@role='radio']")
                        
                        if score <= len(radios_in_group):
                            radios_in_group[score-1].click()
                            print(f"✓ Question {i+1}: Selected score {score}")
                            time.sleep(0.5)
                        
                except Exception as e:
                    print(f"❌ Error with Likert question {i+1}: {e}")
            
            # Scroll down to find essay questions on the same page
            print("Scrolling to find essay questions...")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            
            # Fill essay questions (on the same page as Likert)
            print("Filling essay questions...")
            try:
                # Wait for essay fields to load
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//textarea"))
                )
                
                essay_fields = self.driver.find_elements(By.XPATH, "//textarea")
                print(f"Found {len(essay_fields)} essay fields")
                
                if len(essay_fields) >= 1:
                    essay_fields[0].clear()
                    essay_fields[0].send_keys(data['important_thing'])
                    print("✓ Filled essay question 1")
                    time.sleep(2)
                
                if len(essay_fields) >= 2:
                    essay_fields[1].clear()
                    essay_fields[1].send_keys(data['social_media_role'])
                    print("✓ Filled essay question 2")
                    time.sleep(2)
                    
                if len(essay_fields) >= 3:
                    essay_fields[2].clear()
                    essay_fields[2].send_keys(data['authenticity'])
                    print("✓ Filled essay question 3")
                    time.sleep(2)
                
                # If there are still missing essay fields, try different selectors
                if len(essay_fields) < 3:
                    print("Looking for additional essay fields...")
                    text_inputs = self.driver.find_elements(By.XPATH, "//input[@type='text' and not(@aria-label)]")
                    print(f"Found {len(text_inputs)} additional text inputs")
                    
                    # Try to fill remaining essays in text inputs if needed
                    essay_data = [data['important_thing'], data['social_media_role'], data['authenticity']]
                    filled_count = len(essay_fields)
                    
                    for i, text_input in enumerate(text_inputs):
                        if filled_count < 3 and i < len(essay_data):
                            try:
                                text_input.clear()
                                text_input.send_keys(essay_data[filled_count])
                                print(f"✓ Filled essay question {filled_count + 1} in text input")
                                filled_count += 1
                                time.sleep(2)
                            except:
                                pass
                            
            except Exception as e:
                print(f"❌ Error filling essays: {e}")
            
            # Scroll down and click Next to go to PAGE 3 (Final Submit Page)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            try:
                next_button_2 = WebDriverWait(self.driver, 10).until(
                    EC.any_of(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Berikutnya')]/parent::*")),
                        EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/parent::*")),
                        EC.element_to_be_clickable((By.XPATH, "//div[@role='button'][contains(., 'Next')]"))
                    )
                )
                next_button_2.click()
                print("✓ Navigated to PAGE 3: Final Submit Page")
                time.sleep(4)
            except Exception as e:
                print(f"❌ Error navigating to page 3: {e}")
                return False
            
            print("=== PAGE 3: Final Submit Page ===")
            
            # Scroll down before submitting
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            
            print("=== SUBMITTING FORM ===")
            
            # Submit form with multiple attempts
            try:
                submit_button = WebDriverWait(self.driver, 15).until(
                    EC.any_of(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Kirim')]/parent::*")),
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]/parent::*")),
                        EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//span[contains(text(), 'Kirim')]")),
                        EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//span[contains(text(), 'Submit')]")),
                        EC.element_to_be_clickable((By.XPATH, "//input[@value='Submit']")),
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Submit')]")),
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Kirim')]"))
                    )
                )
                
                # Scroll the submit button into view and click
                self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
                time.sleep(2)
                
                # Try clicking with JavaScript if regular click fails
                try:
                    submit_button.click()
                except:
                    self.driver.execute_script("arguments[0].click();", submit_button)
                
                print("✓ Clicked submit button")
                
                # Wait for confirmation page
                try:
                    WebDriverWait(self.driver, 15).until(
                        EC.any_of(
                            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'terkirim')]")),
                            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'submitted')]")),
                            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Terima kasih')]")),
                            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thank you')]")),
                            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'sehat selalu')]"))
                        )
                    )
                    print("✅ Form submitted successfully!")
                    return True
                except:
                    # If no confirmation found, check URL change
                    time.sleep(3)
                    if "formResponse" in self.driver.current_url:
                        print("✅ Form submitted successfully (URL changed)!")
                        return True
                    else:
                        print("⚠️ Submit clicked but no clear confirmation")
                        return True  # Assume success
                        
            except Exception as e:
                print(f"❌ Error submitting form: {e}")
                
                # Debug information
                print("\n=== DEBUG INFO ===")
                buttons = self.driver.find_elements(By.XPATH, "//div[@role='button']")
                print(f"Available buttons: {len(buttons)}")
                for i, button in enumerate(buttons):
                    try:
                        print(f"  Button {i}: '{button.text}'")
                    except:
                        print(f"  Button {i}: <no text>")
                print("==================\n")
                
                return False
                
        except Exception as e:
            print(f"❌ General error filling form: {e}")
            return False
    # ...existing code...
    def run_multiple_submissions(self, count=10, delay_range=(60, 120)):
        """Submit form multiple times"""
        successful = 0
        
        for i in range(count):
            print(f"\nSubmission {i+1}/{count}")
            
            # Generate new data for each submission
            data = self.generate_random_data()
            print(f"Using name: {data['nama']}")
            
            # Reset to form start
            self.driver.get(self.form_url)
            time.sleep(2)
            
            success = self.fill_form(data)
            
            if success:
                successful += 1
                print(f"✓ Submission {i+1} successful")
            else:
                print(f"✗ Submission {i+1} failed")
            
            # Random delay between submissions
            if i < count - 1:
                delay = random.randint(*delay_range)
                print(f"Waiting {delay} seconds before next submission...")
                time.sleep(delay)
        
        print(f"\nCompleted: {successful}/{count} successful submissions")
        


    def close(self):
        if self.driver:
            self.driver.quit()
            
    def setup_driver(self, debug=True):
        """Setup Chrome WebDriver"""
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        if not debug:
            options.add_argument('--headless')  # Only run headless if not in debug mode
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        
        if debug:
            self.driver.maximize_window()
            

    # Usage

if __name__ == "__main__":
    # Use viewform instead of formResponse
    FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdZQ_h8SCS1izADZrjXI4--SRrDy67Q9CdLiyFNQSIkoDs-2g/viewform"
    
    bot = PersonalBrandingBot(FORM_URL)
    bot.setup_driver()
    
    try:
        # Run 5 submissions with 30-60 second delays
        bot.run_multiple_submissions(count=5, delay_range=(30, 60))
    finally:
        bot.close()