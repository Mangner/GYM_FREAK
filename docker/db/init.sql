-- Włączenie kluczy obcych (w SQLite domyślnie są wyłączone)
PRAGMA foreign_keys = ON;

-- 1. PARTY (Tabela bazowa - Strona/Podmiot)
-- Reprezentuje każdy byt w systemie (Usera lub Grupę)
CREATE TABLE IF NOT EXISTS party (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL CHECK(type IN ('PERSON', 'ORGANIZATION')), -- Rozróżniacz
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 2. PERSON (Osoba - dziedziczy z Party)
-- Dane specyficzne dla użytkownika (SRS: WF-SOCIAL-01)
CREATE TABLE IF NOT EXISTS person (
    party_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    gender TEXT, -- Dane z SRS sekcja 1.3/2.2
    level TEXT, -- Poziom zaawansowania (Beginner, etc.)
    goal TEXT, -- Cel (Redukcja, Masa)
    FOREIGN KEY (party_id) REFERENCES party(id) ON DELETE CASCADE
);

-- 3. ORGANIZATION (Grupa/Siłownia - dziedziczy z Party)
-- Dane specyficzne dla grup (SRS: WF-SOCIAL-10)
CREATE TABLE IF NOT EXISTS organization (
    party_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    FOREIGN KEY (party_id) REFERENCES party(id) ON DELETE CASCADE
);

-- 4. RELATIONSHIP_TYPE (Słownik typów relacji)
CREATE TABLE IF NOT EXISTS relationship_type (
    code TEXT PRIMARY KEY,
    description TEXT
);

-- Wstawiamy domyślne typy relacji z SRS
INSERT OR IGNORE INTO relationship_type (code, description) VALUES 
('FRIENDSHIP', 'Relacja znajomy-znajomy (WF-SOCIAL-08)'),
('MEMBERSHIP', 'Relacja użytkownik należy do grupy (WF-SOCIAL-10)'),
('COACHING', 'Relacja trener-podopieczny (Sekcja 2.2)');

-- 5. PARTY_RELATIONSHIP (Relacje między stronami)
-- Obsługuje zarówno znajomych, jak i przynależność do grup
CREATE TABLE IF NOT EXISTS party_relationship (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_party_id INTEGER NOT NULL, -- Kto inicjuje / Użytkownik
    to_party_id INTEGER NOT NULL,   -- Kogo dotyczy / Drugi User lub Grupa
    type_code TEXT NOT NULL,
    status TEXT DEFAULT 'PENDING', -- PENDING, ACTIVE, BLOCKED
    start_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (from_party_id) REFERENCES party(id),
    FOREIGN KEY (to_party_id) REFERENCES party(id),
    FOREIGN KEY (type_code) REFERENCES relationship_type(code)
);