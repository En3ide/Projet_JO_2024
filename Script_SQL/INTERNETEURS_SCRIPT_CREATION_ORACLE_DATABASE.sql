--
-- Base de données : Projet_JO_2024
--

--
-- Structure de la table Athlete
--

DROP TABLE Athlete CASCADE CONSTRAINTS;
CREATE TABLE Athlete (
  id_athlete NUMBER PRIMARY KEY,
  firstname_athlete VARCHAR2(50) NOT NULL,
  name_athlete VARCHAR2(50) NOT NULL,
  birthday_athlete DATE DEFAULT NULL,
  gender_athlete VARCHAR2(10) NOT NULL CHECK (gender_athlete IN ('MAN', 'WOMAN')),
  code_country CHAR(3) DEFAULT NULL,
  CONSTRAINT fk_athlete_country FOREIGN KEY (code_country) REFERENCES Country(code_country)
);

-- --------------------------------------------------------

--
-- Structure de la table Country
--

DROP TABLE Country CASCADE CONSTRAINTS;
CREATE TABLE Country (
  code_country CHAR(3) PRIMARY KEY,
  name_country VARCHAR2(50) NOT NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Date_calendar
--

DROP TABLE Date_calendar CASCADE CONSTRAINTS;
CREATE TABLE Date_calendar (
  id_date_cal NUMBER PRIMARY KEY,
  date_cal DATE NOT NULL,
  medal_ceremony_date_cal NUMBER(1) NOT NULL DEFAULT 0
);

-- --------------------------------------------------------

--
-- Structure de la table Discipline
--

DROP TABLE Discipline CASCADE CONSTRAINTS;
CREATE TABLE Discipline (
  id_disc NUMBER PRIMARY KEY,
  name_fr_disc VARCHAR2(50) NOT NULL,
  name_an_disc VARCHAR2(50),
  category_disc VARCHAR2(20) NOT NULL CHECK (category_disc IN ('OLYMPIC', 'PARALYMPIC'))
);

-- --------------------------------------------------------

--
-- Structure de la table Event
--

DROP TABLE Event CASCADE CONSTRAINTS;
CREATE TABLE Event (
  id_event NUMBER PRIMARY KEY,
  name_event VARCHAR2(50) NOT NULL,
  format_event VARCHAR2(20) NOT NULL CHECK (format_event IN ('INDIVIDUAL', 'COLLECTIVE', 'HYBRID')),
  gender_event VARCHAR2(10) NOT NULL CHECK (gender_event IN ('MAN', 'WOMAN', 'MIXED')),
  id_disc NUMBER NOT NULL,
  id_record NUMBER DEFAULT NULL,
  CONSTRAINT fk_event_discipline FOREIGN KEY (id_disc) REFERENCES Discipline(id_disc),
  CONSTRAINT fk_event_record FOREIGN KEY (id_record) REFERENCES Record(id_record)
);

-- --------------------------------------------------------

--
-- Structure de la table Medal
--

DROP TABLE Medal CASCADE CONSTRAINTS;
CREATE TABLE Medal (
  id_medal NUMBER PRIMARY KEY,
  type_medal VARCHAR2(10) NOT NULL CHECK (type_medal IN ('GOLD','SILVER','BRONZE')),
  id_event NUMBER NOT NULL,
  id_athlete NUMBER DEFAULT NULL,
  id_date_cal NUMBER DEFAULT NULL,
  CONSTRAINT fk_medal_event FOREIGN KEY (id_event) REFERENCES Event(id_event),
  CONSTRAINT fk_medal_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete(id_athlete),
  CONSTRAINT fk_medal_date_calendar FOREIGN KEY (id_date_cal) REFERENCES Date_calendar(id_date_cal)
);

-- --------------------------------------------------------

--
-- Structure de la table Record
--

DROP TABLE Record CASCADE CONSTRAINTS;
CREATE TABLE Record (
  id_record NUMBER PRIMARY KEY,
  stat_record VARCHAR2(32) NOT NULL,
  date_record DATE,
  id_event NUMBER DEFAULT NULL,
  id_athlete NUMBER DEFAULT NULL,
  CONSTRAINT fk_record_event FOREIGN KEY (id_event) REFERENCES Event(id_event),
  CONSTRAINT fk_record_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete(id_athlete)
);

-- --------------------------------------------------------

--
-- Structure de la table Transport
--

DROP TABLE Transport CASCADE CONSTRAINTS;
CREATE TABLE Transport (
  id_trans NUMBER PRIMARY KEY,
  name_trans VARCHAR2(20) NOT NULL CHECK (name_trans IN ('TRAIN', 'TRAMWAY', 'BUS', 'METRO'))
);

-- --------------------------------------------------------

--
-- Structure de la table Site
--

DROP TABLE Site CASCADE CONSTRAINTS;
CREATE TABLE Site (
  id_site NUMBER PRIMARY KEY,
  name_site VARCHAR2(50) NOT NULL,
  adress_site VARCHAR2(50) NOT NULL,
  creation_date_site DATE DEFAULT NULL,
  capacity_site NUMBER DEFAULT NULL,
  URL_site VARCHAR2(255) DEFAULT NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Team
--

DROP TABLE Team CASCADE CONSTRAINTS;
CREATE TABLE Team (
  id_team NUMBER PRIMARY KEY,
  size_team NUMBER NOT NULL,
  gender_team VARCHAR2(10) NOT NULL CHECK (gender_team IN ('MAN', 'WOMAN', 'MIXED')),
  code_country CHAR(3) DEFAULT NULL,
  CONSTRAINT fk_team_country FOREIGN KEY (code_country) REFERENCES Country(code_country)
);

-- --------------------------------------------------------

--
-- Structure de la table Is_from
--

DROP TABLE Is_from CASCADE CONSTRAINTS;
CREATE TABLE Is_from (
  id_athlete NUMBER NOT NULL,
  code_country CHAR(3) NOT NULL,
  CONSTRAINT pk_is_from PRIMARY KEY (id_athlete, code_country),
  CONSTRAINT fk_is_from_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete(id_athlete),
  CONSTRAINT fk_is_from_country FOREIGN KEY (code_country) REFERENCES Country(code_country)
);

-- --------------------------------------------------------

--
-- Structure de la table To_pertain_team
--

DROP TABLE To_pertain_team CASCADE CONSTRAINTS;
CREATE TABLE To_pertain_team (
  id_athlete NUMBER NOT NULL,
  id_team NUMBER NOT NULL,
  CONSTRAINT pk_to_pertain_team PRIMARY KEY (id_athlete, id_team),
  CONSTRAINT fk_to_pertain_team_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete(id_athlete),
  CONSTRAINT fk_to_pertain_team_team FOREIGN KEY (id_team) REFERENCES Team(id_team)
);

-- --------------------------------------------------------

--
-- Structure de la table To_Register_athlete
--

DROP TABLE To_Register_athlete CASCADE CONSTRAINTS;
CREATE TABLE To_Register_athlete (
  id_event NUMBER NOT NULL,
  id_athlete NUMBER NOT NULL,
  CONSTRAINT pk_to_register_athlete PRIMARY KEY (id_event, id_athlete),
  CONSTRAINT fk_to_register_athlete_event FOREIGN KEY (id_event) REFERENCES Event(id_event),
  CONSTRAINT fk_to_register_athlete_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete(id_athlete)
);

-- --------------------------------------------------------

--
-- Structure de la table To_Register_team
--

DROP TABLE To_Register_team CASCADE CONSTRAINTS;
CREATE TABLE To_Register_team (
  id_event NUMBER NOT NULL,
  id_team NUMBER NOT NULL,
  CONSTRAINT pk_to_register_team PRIMARY KEY (id_event, id_team),
  CONSTRAINT fk_to_register_team_event FOREIGN KEY (id_event) REFERENCES Event(id_event),
  CONSTRAINT fk_to_register_team_team FOREIGN KEY (id_team) REFERENCES Team(id_team)
);

-- --------------------------------------------------------

--
-- Structure de la table To_Schedule
--

DROP TABLE To_Schedule CASCADE CONSTRAINTS;
CREATE TABLE To_Schedule (
  id_site NUMBER NOT NULL,
  id_date_cal NUMBER NOT NULL,
  id_event NUMBER NOT NULL,
  CONSTRAINT pk_to_schedule PRIMARY KEY (id_site, id_date_cal, id_event),
  CONSTRAINT fk_to_schedule_site FOREIGN KEY (id_site) REFERENCES Site(id_site),
  CONSTRAINT fk_to_schedule_date_calendar FOREIGN KEY (id_date_cal) REFERENCES Date_calendar(id_date_cal),
  CONSTRAINT fk_to_schedule_event FOREIGN KEY (id_event) REFERENCES Event(id_event)
);

-- --------------------------------------------------------

--
-- Structure de la table To_Serve
--

DROP TABLE To_Serve CASCADE CONSTRAINTS;
CREATE TABLE To_Serve (
  id_site NUMBER NOT NULL,
  id_trans NUMBER NOT NULL,
  num_ligne VARCHAR2(50) NOT NULL,
  station_name VARCHAR2(50) NOT NULL,
  CONSTRAINT pk_to_serve PRIMARY KEY (id_site, id_trans),
  CONSTRAINT fk_to_serve_site FOREIGN KEY (id_site) REFERENCES Site(id_site),
  CONSTRAINT fk_to_serve_transport FOREIGN KEY (id_trans) REFERENCES Transport(id_trans)
);