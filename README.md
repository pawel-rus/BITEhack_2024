# BITEhack_2024 / Senior Assistant AI

Senior Assistant AI to innowacyjna aplikacja zaprojektowana, aby zamazać przepaść między seniorami a nowoczesną technologią i ułatwić życie naszym kochanym staruszkom w tym niełatwym i biegnącym coraz szybciej świecie. Dzięki intuicyjnym rozwiązaniom aplikacja umożliwia seniorom wygodne korzystanie z technologii i czerpanie z niej korzyści w codziennym życiu.

## Kluczowe funkcje

### Architektura mikroserwisów
Nasza aplikacja wykorzystuje architekturę mikroserwisów, co pozwala na niezależne tworzenie, wdrażanie i utrzymanie każdego komponentu. Takie podejście zapewnia:
- **Skalowalność**
- **Izolacja błędów**
- **Elastyczność**

### Zaawansowana AI z technologią RAG
Wdrożyliśmy **Retrieval-Augmented Generation (RAG)**, aby dostarczać dokładne i kontekstowe odpowiedzi. Dzięki wykorzystaniu struktury danych `TextNodes` z metadanymi, zawierającej popularne problemy seniorów oraz sprawdzone rozwiązania, aplikacja oferuje:
- Szybki dostęp do przydatnych informacji.
- Odpowiednie wskazówki dostosowane do potrzeb seniorów.

### Wykorzystane modele
Aplikacja korzysta z najnowocześniejszych modeli AI, aby zapewnić najwyższą jakość działania:
- **LLama-3.1-8B-Instant**
- **Google-Gemini-1.5**
- **BAAI/bge-small-en-v1.5** (model embeddingowy z HuggingFace)

Te modele wspólnie zwiększają zdolność aplikacji do rozumienia, wyszukiwania i generowania trafnych informacji z niezwykłą precyzją.

### Stos technologiczny
- **Frontend:** React
- **Backend:** Flask
- **Baza danych:** Zdalny PostgreSQL

---

## Instrukcja instalacji

### Wymagania
Aby uruchomić aplikację, wymagane są:
- **Python 3.12**
- **Node.js**
- **Pip**
- **NPM**
- **Google Colab** (do indeksowania bazy danych przy użyciu GPU)

### Instalacja

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/your-repository/senior-assistant-ai.git
   cd senior-assistant-ai
   ```

2. Zainstaluj zależności backendu:
   ```bash
   pip install -r requirements.txt
   ```

3. Zainstaluj zależności frontendowe:
   ```bash
   cd frontend
   npm install
   ```

4. Uruchom aplikację React:
   ```bash
   npm start
   ```

5. Uruchom mikroserwisy (każdy w osobnym terminalu):
   - API Gateway:
     ```bash
     cd api-gateway
     python3 app.py
     ```
   - Chatbot Service:
     ```bash
     cd chatbot_service
     python3 app.py
     ```
   - Education Service:
     ```bash
     cd education_service
     python3 app.py
     ```
   - Helpdesk Service:
     ```bash
     cd helpdesk_service
     python3 app.py
     ```

### Alternatywa: Uruchomienie za pomocą Docker Compose
Jeśli preferujesz w pełni zintegrowane środowisko, możesz użyć Docker Compose:

1. Upewnij się, że masz zainstalowanego Dockera oraz Docker Compose.
2. Uruchom komendę:
   ```bash
   docker-compose up
   ```

Docker-Compose automatycznie uruchomi wszystkie mikroserwisy oraz frontend w zintegrowanym środowisku.

---

Serdecznie zachęcamy do kontaktu z nami!

<br>
<br>
<br>


![zdj](https://scontent.xx.fbcdn.net/v/t1.15752-9/472924707_564705353109915_3298643274248233454_n.png?stp=dst-png_s720x720&_nc_cat=100&ccb=1-7&_nc_sid=0024fc&_nc_ohc=RT9qg67WaUYQ7kNvgG2vnKi&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1gGFY32R2QBjuc7ZRv1ie6rN40oWdpfzv2Mk7cWREBYMoQ&oe=67A38027)
![zdj](https://scontent.xx.fbcdn.net/v/t1.15752-9/472198903_1291905752145030_6620408180174984424_n.png?stp=dst-png_s720x720&_nc_cat=104&ccb=1-7&_nc_sid=0024fc&_nc_ohc=D6aVxh70eYwQ7kNvgGgTuBe&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1gF8qIXQn_suKK0c_y5a6erQWaCUIJ_mVkjtRZ4DiFdswQ&oe=67A3A65A)
![zdj](https://scontent.xx.fbcdn.net/v/t1.15752-9/472995131_415907804845414_6148629235314706125_n.png?stp=dst-png_s720x720&_nc_cat=109&ccb=1-7&_nc_sid=0024fc&_nc_ohc=VsDsyxxRe3QQ7kNvgH7UqtU&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1gGLhR891ITxz0aJbxUl_NTTWpHF7t8NDlJzpga7MBJ-TQ&oe=67A3A5E8)
![zdj](https://scontent.xx.fbcdn.net/v/t1.15752-9/472091751_1502650507098525_6101531369062923946_n.png?stp=dst-png_s720x720&_nc_cat=104&ccb=1-7&_nc_sid=0024fc&_nc_ohc=zfjinCju-KIQ7kNvgGXA5aF&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1gGJn0HKWz1DjvSw9t8L0bkfZfjw5h304PyIJc3Jgy6bRg&oe=67A3919A)
![zdj](https://scontent.xx.fbcdn.net/v/t1.15752-9/472334007_934542745459669_6384721517262523045_n.png?stp=dst-png_s720x720&_nc_cat=102&ccb=1-7&_nc_sid=0024fc&_nc_ohc=n2ZLBZRKZssQ7kNvgGKVZLl&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1gEbbUxwcdqxOKMPw2berN8Qyd4h3DI-bH7oNv4D66iFHQ&oe=67A3A216)
![zdj](https://scontent.xx.fbcdn.net/v/t1.15752-9/472398647_1814787362665646_5392335792685766580_n.png?stp=dst-png_s720x720&_nc_cat=108&ccb=1-7&_nc_sid=0024fc&_nc_ohc=QaFK87QnLAoQ7kNvgEgshjE&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1gHD_2CpDZht1cAKLnVXSezu7cWd5ewFGD1z7f4O5_Mp9w&oe=67A37639)
