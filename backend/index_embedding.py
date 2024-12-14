from llama_index.core.schema import TextNode
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, VectorStoreIndex

def create_llama_index():
    try:
        index_dir = './final_index'  # Specify the directory your index will be stored
        
        nodes = [
            TextNode(
                text="Nie mogę zalogować się do bankowości internetowej.",
                metadata={
                    "kategoria": "Bankowość online",
                    "rozwiązanie": "Sprawdź poprawność loginu i hasła, użyj opcji przypomnienia hasła, lub skontaktuj się z bankiem.",
                    "gdzie mogę udać się po pomoc": "Obsługa klienta banku, rodzina, znajomi, infolinia banku.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, z pomocą infolinii banku.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Średnie",
                    "prawdopodobieństwo scamu": "Średnie",
                    "gdzie mogę zweryfikować": "Oficjalna strona banku, infolinia banku."
                }
            ),
            TextNode(
                text="Otrzymałem podejrzany e-mail od 'banku' proszący o podanie danych logowania.",
                metadata={
                    "kategoria": "Phishing",
                    "rozwiązanie": "Nie klikaj w żadne linki i nie podawaj danych. Zgłoś wiadomość do banku.",
                    "gdzie mogę udać się po pomoc": "Infolinia banku, specjalista IT, rodzina.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, kontaktując się z infolinią banku.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Bardzo wysokie",
                    "prawdopodobieństwo scamu": "Bardzo wysokie",
                    "gdzie mogę zweryfikować": "Oficjalna strona banku, infolinia banku."
                }
            ),
            TextNode(
                text="Nie wiem, jak zainstalować aplikację na smartfonie.",
                metadata={
                    "kategoria": "Użycie smartfona",
                    "rozwiązanie": "Przejdź do sklepu z aplikacjami (Google Play lub App Store), wyszukaj aplikację i kliknij 'Zainstaluj'.",
                    "gdzie mogę udać się po pomoc": "Rodzina, znajomi, punkt obsługi klienta operatora telefonu.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, z pomocą kogoś, kto zna obsługę smartfona.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Niskie",
                    "prawdopodobieństwo scamu": "Niskie",
                    "gdzie mogę zweryfikować": "Instrukcja obsługi telefonu, autoryzowane punkty obsługi."
                }
            ),
            TextNode(
                text="Nie umiem ustawić wideorozmowy na smartfonie.",
                metadata={
                    "kategoria": "Komunikacja online",
                    "rozwiązanie": "Zainstaluj aplikację do wideorozmów (np. Skype, WhatsApp), zaloguj się i wybierz rozmówcę, klikając ikonę kamery.",
                    "gdzie mogę udać się po pomoc": "Rodzina, znajomi, lokalne centrum seniora.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, ale tylko częściowo.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Niskie",
                    "prawdopodobieństwo scamu": "Niskie",
                    "gdzie mogę zweryfikować": "Instrukcje online, lokalne centrum pomocy technologicznej."
                }
            ),
            TextNode(
                text="Nie wiem, jak połączyć się z Wi-Fi w domu.",
                metadata={
                    "kategoria": "Łączność internetowa",
                    "rozwiązanie": "Otwórz ustawienia Wi-Fi na urządzeniu, wybierz swoją sieć i wpisz hasło.",
                    "gdzie mogę udać się po pomoc": "Rodzina, dostawca internetu, lokalny serwis IT.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, jeśli ktoś poprowadzi Cię krok po kroku.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Niskie",
                    "prawdopodobieństwo scamu": "Niskie",
                    "gdzie mogę zweryfikować": "Instrukcja routera, dostawca internetu."
                }
            ),
            TextNode(
                text="Nie mogę otworzyć plików PDF na komputerze.",
                metadata={
                    "kategoria": "Obsługa plików",
                    "rozwiązanie": "Zainstaluj program do odczytu PDF, np. Adobe Reader lub inny darmowy czytnik.",
                    "gdzie mogę udać się po pomoc": "Rodzina, znajomi, lokalny serwis IT.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, z pomocą kogoś bardziej zaawansowanego technologicznie.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Niskie",
                    "prawdopodobieństwo scamu": "Niskie",
                    "gdzie mogę zweryfikować": "Oficjalna strona producenta oprogramowania PDF."
                }
            ),
            TextNode(
                text="Komputer działa wolno i zawiesza się.",
                metadata={
                    "kategoria": "Wydajność komputera",
                    "rozwiązanie": "Uruchom program antywirusowy, zamknij niepotrzebne aplikacje, zaktualizuj system operacyjny.",
                    "gdzie mogę udać się po pomoc": "Lokalny serwis komputerowy, rodzina, znajomi.",
                    "czy można taki problem rozwiązać przez telefon": "Częściowo, jeśli ktoś doradzi odpowiednie kroki.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Średnie",
                    "prawdopodobieństwo scamu": "Średnie",
                    "gdzie mogę zweryfikować": "Oficjalne strony producentów oprogramowania."
                }
            ),
            TextNode(
                text="Nie mogę znaleźć zdjęć na smartfonie.",
                metadata={
                    "kategoria": "Zarządzanie plikami",
                    "rozwiązanie": "Otwórz aplikację Galeria lub Zdjęcia i przejrzyj foldery.",
                    "gdzie mogę udać się po pomoc": "Rodzina, znajomi, lokalne centrum pomocy technologicznej.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, z pomocą kogoś, kto zna system smartfona.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Niskie",
                    "prawdopodobieństwo scamu": "Niskie",
                    "gdzie mogę zweryfikować": "Instrukcja telefonu, obsługa klienta producenta."
                }
            ),
            TextNode(
                text="Dostałem telefon od 'Microsoftu', który twierdzi, że mam wirusa na komputerze.",
                metadata={
                    "kategoria": "Oszustwa telefoniczne",
                    "rozwiązanie": "Natychmiast zakończ rozmowę i nie podawaj żadnych danych.",
                    "gdzie mogę udać się po pomoc": "Rodzina, znajomi, lokalne centrum pomocy IT.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, informując odpowiednie służby o oszustwie.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Bardzo wysokie",
                    "prawdopodobieństwo scamu": "Bardzo wysokie",
                    "gdzie mogę zweryfikować": "Oficjalna strona Microsoftu, lokalne władze."
                }
            ),
            TextNode(
                text="Nie wiem, jak ustawić alarm na telefonie.",
                metadata={
                    "kategoria": "Funkcje smartfona",
                    "rozwiązanie": "Otwórz aplikację Zegar, wybierz opcję Alarm i ustaw godzinę.",
                    "gdzie mogę udać się po pomoc": "Rodzina, znajomi, lokalne centrum pomocy technologicznej.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, z pomocą kogoś, kto zna obsługę smartfona.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Niskie",
                    "prawdopodobieństwo scamu": "Niskie",
                    "gdzie mogę zweryfikować": "Instrukcja telefonu."
                }
            ),
            TextNode(
                text="Nie mogę wysłać wiadomości e-mail na komputerze.",
                metadata={
                    "kategoria": "Komunikacja internetowa",
                    "rozwiązanie": "Sprawdź ustawienia poczty, upewnij się, że masz połączenie internetowe, zweryfikuj adres e-mail.",
                    "gdzie mogę udać się po pomoc": "Rodzina, znajomi, punkt obsługi internetu, infolinia dostawcy usług.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, z pomocą specjalisty IT.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Niskie",
                    "prawdopodobieństwo scamu": "Niskie",
                    "gdzie mogę zweryfikować": "Oficjalna strona usługi pocztowej."
                }
            ),
            TextNode(
                text="Nie rozumiem, jak korzystać z portalu społecznościowego.",
                metadata={
                    "kategoria": "Media społecznościowe",
                    "rozwiązanie": "Zaloguj się na stronę, obejrzyj tutorial wprowadzający, zaprzyjaźnij się z podstawowymi funkcjami.",
                    "gdzie mogę udać się po pomoc": "Młodsi krewni, lokalne centrum komputerowe, kursy dla seniorów.",
                    "czy można taki problem rozwiązać przez telefon": "Częściowo, poprzez prowadzenie przez telefon.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Średnie",
                    "prawdopodobieństwo scamu": "Średnie",
                    "gdzie mogę zweryfikować": "Oficjalna strona portalu społecznościowego, pomoc techniczna."
                }
            ),
            TextNode(
                text="Mam problemy z drukowaniem dokumentów.",
                metadata={
                    "kategoria": "Sprzęt biurowy",
                    "rozwiązanie": "Sprawdź podłączenie drukarki, upewnij się, że jest włączona, zainstaluj sterowniki.",
                    "gdzie mogę udać się po pomoc": "Serwis komputerowy, sklep z elektroniką, rodzina.",
                    "czy można taki problem rozwiązać przez telefon": "Częściowo, z pomocą specjalisty.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Niskie",
                    "prawdopodobieństwo scamu": "Niskie",
                    "gdzie mogę zweryfikować": "Strona producenta drukarki, pomoc techniczna."
                }
            ),
            TextNode(
                text="Ktoś dzwoni i prosi o dostęp do mojego komputera zdalnego.",
                metadata={
                    "kategoria": "Bezpieczeństwo internetowe",
                    "rozwiązanie": "Nie zgadzaj się na żadne zdalne połączenia, przerwij rozmowę, zgłoś próbę oszustwa.",
                    "gdzie mogę udać się po pomoc": "Policja, rodzina, lokalne centrum bezpieczeństwa cybernetycznego.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, informując odpowiednie służby.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Bardzo wysokie",
                    "prawdopodobieństwo scamu": "Bardzo wysokie",
                    "gdzie mogę zweryfikować": "Oficjalne strony antywirusowe, policja."
                }
            ),
            TextNode(
                text="Nie mogę zaktualizować systemu operacyjnego.",
                metadata={
                    "kategoria": "Aktualizacje oprogramowania",
                    "rozwiązanie": "Sprawdź połączenie internetowe, zwolnij miejsce na dysku, uruchom aktualizację ręcznie.",
                    "gdzie mogę udać się po pomoc": "Lokalny serwis komputerowy, rodzina, forum internetowe.",
                    "czy można taki problem rozwiązać przez telefon": "Częściowo, z prowadzeniem krok po kroku.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Niskie",
                    "prawdopodobieństwo scamu": "Niskie",
                    "gdzie mogę zweryfikować": "Oficjalna strona producenta systemu."
                }
            ),
            TextNode(
                text="Nie wiem, jak zrobić zrzut ekranu.",
                metadata={
                    "kategoria": "Podstawowe umiejętności komputerowe",
                    "rozwiązanie": "Naciśnij klawisz 'Print Screen' lub kombinację klawiszy Windows + Print Screen, aby zrobić zrzut ekranu.",
                    "gdzie mogę udać się po pomoc": "Rodzina, kursy komputerowe, lokalne centrum dla seniorów.",
                    "czy można taki problem rozwiązać przez telefon": "Tak, poprzez dokładne instrukcje.",
                    "prawdopodobieństwo, że ktoś chce mnie oszukać": "Niskie",
                    "prawdopodobieństwo scamu": "Niskie",
                    "gdzie mogę zweryfikować": "Oficjalna pomoc systemu operacyjnego."
                }
            )
        ]

        
        embed_model = HuggingFaceEmbedding( model_name="BAAI/bge-small-en-v1.5")
        index=VectorStoreIndex(nodes, embed_model=embed_model)
        Settings.embed_model = embed_model
        
        index.storage_context.persist(persist_dir=index_dir)

        return print({'result': 'File indexed successfully'})
    except Exception as e:
        return print({'error':  f"An error occurred: {e}"})
    
create_llama_index()