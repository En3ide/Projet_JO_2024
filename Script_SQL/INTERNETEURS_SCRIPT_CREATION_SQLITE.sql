PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

--
-- Base de données : Projet_JO_2024
--

--
-- Structure de la table Athlete
--

DROP TABLE IF EXISTS Athlete;
CREATE TABLE Athlete (
  id_athlete INTEGER PRIMARY KEY AUTOINCREMENT,
  firstname_athlete VARCHAR(50) NOT NULL,
  name_athlete VARCHAR(50) NOT NULL,
  birthday_athlete DATE DEFAULT NULL,
  gender_athlete TEXT NOT NULL CHECK (gender_athlete IN ('MAN', 'WOMAN')),
  code_country CHAR(3) DEFAULT NULL,
  FOREIGN KEY (code_country) REFERENCES Country(code_country)
);

-- --------------------------------------------------------

--
-- Structure de la table Country
--

DROP TABLE IF EXISTS Country;
CREATE TABLE Country (
  code_country CHAR(3) PRIMARY KEY,
  name_country VARCHAR(50) NOT NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Date_calendar
--

DROP TABLE IF EXISTS Date_calendar;
CREATE TABLE Date_calendar (
  id_date_cal INTEGER PRIMARY KEY AUTOINCREMENT,
  date_cal DATE NOT NULL,
  medal_ceremony_date_cal INTEGER NOT NULL DEFAULT 0
);

-- --------------------------------------------------------

--
-- Structure de la table Discipline
--

DROP TABLE IF EXISTS Discipline;
CREATE TABLE Discipline (
  id_disc INTEGER PRIMARY KEY AUTOINCREMENT,
  name_fr_disc VARCHAR(50) NOT NULL,
  name_an_disc VARCHAR(50),
  category_disc TEXT NOT NULL CHECK (category_disc IN ('OLYMPIC', 'PARALYMPIC'))
);

-- --------------------------------------------------------

--
-- Structure de la table Event
--

DROP TABLE IF EXISTS Event;
CREATE TABLE Event (
  id_event INTEGER PRIMARY KEY AUTOINCREMENT,
  name_event VARCHAR(50) NOT NULL,
  format_event TEXT NOT NULL CHECK (format_event IN ('INDIVIDUAL', 'COLLECTIVE', 'HYBRID')),
  gender_event TEXT NOT NULL CHECK (gender_event IN ('MAN', 'WOMAN', 'MIXED')),
  id_disc INTEGER NOT NULL,
  id_record INTEGER DEFAULT NULL,
  FOREIGN KEY (id_disc) REFERENCES Discipline(id_disc),
  FOREIGN KEY (id_record) REFERENCES Record(id_record)
);

-- --------------------------------------------------------

--
-- Structure de la table Medal
--

DROP TABLE IF EXISTS Medal;
CREATE TABLE Medal (
  id_medal INTEGER PRIMARY KEY AUTOINCREMENT,
  type_medal TEXT NOT NULL CHECK (type_medal IN ('GOLD','SILVER','BRONZE')),
  id_event INTEGER NOT NULL,
  id_athlete INTEGER DEFAULT NULL,
  id_date_cal INTEGER DEFAULT NULL,
  FOREIGN KEY (id_event) REFERENCES Event(id_event),
  FOREIGN KEY (id_athlete) REFERENCES Athlete(id_athlete),
  FOREIGN KEY (id_date_cal) REFERENCES Date_calendar(id_date_cal)
);

-- --------------------------------------------------------

--
-- Structure de la table Record
--

DROP TABLE IF EXISTS Record;
CREATE TABLE Record (
  id_record INTEGER PRIMARY KEY AUTOINCREMENT,
  stat_record VARCHAR(32) NOT NULL,
  date_record DATE,
  id_event INTEGER DEFAULT NULL,
  id_athlete INTEGER DEFAULT NULL,
  FOREIGN KEY (id_event) REFERENCES Event(id_event),
  FOREIGN KEY (id_athlete) REFERENCES Athlete(id_athlete)
);

-- --------------------------------------------------------

--
-- Structure de la table Transport
--

DROP TABLE IF EXISTS Transport;
CREATE TABLE Transport (
  id_trans INTEGER PRIMARY KEY AUTOINCREMENT,
  name_trans TEXT NOT NULL CHECK (name_trans IN ('TRAIN', 'TRAMWAY', 'BUS', 'METRO'))
);

-- --------------------------------------------------------

--
-- Structure de la table Site
--

DROP TABLE IF EXISTS Site;
CREATE TABLE Site (
  id_site INTEGER PRIMARY KEY AUTOINCREMENT,
  name_site VARCHAR(50) NOT NULL,
  adress_site VARCHAR(50) NOT NULL,
  creation_date_site DATE DEFAULT NULL,
  capacity_site INTEGER DEFAULT NULL,
  URL_site VARCHAR(255) DEFAULT NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Team
--

DROP TABLE IF EXISTS Team;
CREATE TABLE Team (
  id_team INTEGER PRIMARY KEY AUTOINCREMENT,
  size_team INTEGER NOT NULL,
  gender_team TEXT NOT NULL CHECK (gender_team IN ('MAN', 'WOMAN', 'MIXED')),
  code_country CHAR(3) DEFAULT NULL,
  FOREIGN KEY (code_country) REFERENCES Country(code_country)
);

-- --------------------------------------------------------

--
-- Structure de la table Is_from
--

DROP TABLE IF EXISTS Is_from;
CREATE TABLE Is_from (
  id_athlete INTEGER NOT NULL,
  code_country CHAR(3) NOT NULL,
  PRIMARY KEY (id_athlete, code_country),
  FOREIGN KEY (id_athlete) REFERENCES Athlete(id_athlete),
  FOREIGN KEY (code_country) REFERENCES Country(code_country)
);

-- --------------------------------------------------------

--
-- Structure de la table To_pertain_team
--

DROP TABLE IF EXISTS To_pertain_team;
CREATE TABLE To_pertain_team (
  id_athlete INTEGER NOT NULL,
  id_team INTEGER NOT NULL,
  PRIMARY KEY (id_athlete, id_team),
  FOREIGN KEY (id_athlete) REFERENCES Athlete(id_athlete),
  FOREIGN KEY (id_team) REFERENCES Team(id_team)
);

-- --------------------------------------------------------

--
-- Structure de la table To_Register_athlete
--

DROP TABLE IF EXISTS To_Register_athlete;
CREATE TABLE To_Register_athlete (
  id_event INTEGER NOT NULL,
  id_athlete INTEGER NOT NULL,
  PRIMARY KEY (id_event, id_athlete),
  FOREIGN KEY (id_event) REFERENCES Event(id_event),
  FOREIGN KEY (id_athlete) REFERENCES Athlete(id_athlete)
);

-- --------------------------------------------------------

--
-- Structure de la table To_Register_team
--

DROP TABLE IF EXISTS To_Register_team;
CREATE TABLE To_Register_team (
  id_event INTEGER NOT NULL,
  id_team INTEGER NOT NULL,
  PRIMARY KEY (id_event, id_team),
  FOREIGN KEY (id_event) REFERENCES Event(id_event),
  FOREIGN KEY (id_team) REFERENCES Team(id_team)
);

-- --------------------------------------------------------

--
-- Structure de la table To_Schedule
--

DROP TABLE IF EXISTS To_Schedule;
CREATE TABLE To_Schedule (
  id_site INTEGER NOT NULL,
  id_date_cal INTEGER NOT NULL,
  id_event INTEGER NOT NULL,
  PRIMARY KEY (id_site, id_date_cal, id_event),
  FOREIGN KEY (id_site) REFERENCES Site(id_site),
  FOREIGN KEY (id_date_cal) REFERENCES Date_calendar(id_date_cal),
  FOREIGN KEY (id_event) REFERENCES Event(id_event)
);

-- --------------------------------------------------------

--
-- Structure de la table To_Serve
--

DROP TABLE IF EXISTS To_Serve;
CREATE TABLE To_Serve (
  id_site INTEGER NOT NULL,
  id_trans INTEGER NOT NULL,
  num_ligne VARCHAR(50) NOT NULL,
  station_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_site, id_trans),
  FOREIGN KEY (id_site) REFERENCES Site(id_site),
  FOREIGN KEY (id_trans) REFERENCES Transport(id_trans)
);

COMMIT;
