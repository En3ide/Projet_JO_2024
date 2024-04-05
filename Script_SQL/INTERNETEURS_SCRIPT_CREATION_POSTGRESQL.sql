--
-- Structure de la table Athlete
--

DROP TABLE IF EXISTS Athlete;
CREATE TABLE Athlete (
  id_athlete SERIAL PRIMARY KEY,
  firstname_athlete VARCHAR(50) NOT NULL,
  name_athlete VARCHAR(50) NOT NULL,
  birthday_athlete date DEFAULT NULL,
  gender_athlete VARCHAR(7) NOT NULL,
  code_country char(3) DEFAULT NULL,
  CONSTRAINT fk_athlete_country FOREIGN KEY (code_country) REFERENCES Country (code_country) ON DELETE SET NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Country
--

DROP TABLE IF EXISTS Country;
CREATE TABLE Country (
  code_country char(3) PRIMARY KEY,
  name_country VARCHAR(50) NOT NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Date_calendar
--

DROP TABLE IF EXISTS Date_calendar;
CREATE TABLE Date_calendar (
  id_date_cal SERIAL PRIMARY KEY,
  date_cal date NOT NULL,
  medal_ceremony_date_cal boolean NOT NULL DEFAULT false
);

-- --------------------------------------------------------

--
-- Structure de la table Discipline
--

DROP TABLE IF EXISTS Discipline;
CREATE TABLE Discipline (
  id_disc SERIAL PRIMARY KEY,
  name_fr_disc VARCHAR(50) NOT NULL,
  name_an_disc VARCHAR(50),
  category_disc VARCHAR(10) NOT NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Event
--

DROP TABLE IF EXISTS Event;
CREATE TABLE Event (
  id_event SERIAL PRIMARY KEY,
  name_event VARCHAR(50) NOT NULL,
  format_event VARCHAR(10) NOT NULL,
  gender_event VARCHAR(6) NOT NULL,
  id_disc INT NOT NULL,
  id_record INT DEFAULT NULL,
  CONSTRAINT fk_event_discipline FOREIGN KEY (id_disc) REFERENCES Discipline (id_disc) ON DELETE CASCADE,
  CONSTRAINT fk_event_record FOREIGN KEY (id_record) REFERENCES Record (id_record) ON DELETE SET NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Medal
--

DROP TABLE IF EXISTS Medal;
CREATE TABLE Medal (
  id_medal SERIAL PRIMARY KEY,
  type_medal VARCHAR(6) NOT NULL,
  id_event INT NOT NULL,
  id_athlete INT DEFAULT NULL,
  id_date_cal INT DEFAULT NULL,
  CONSTRAINT fk_medal_event FOREIGN KEY (id_event) REFERENCES Event (id_event) ON DELETE CASCADE,
  CONSTRAINT fk_medal_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete (id_athlete) ON DELETE SET NULL,
  CONSTRAINT fk_medal_date_calendar FOREIGN KEY (id_date_cal) REFERENCES Date_calendar (id_date_cal) ON DELETE SET NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Record
--

DROP TABLE IF EXISTS Record;
CREATE TABLE Record (
  id_record SERIAL PRIMARY KEY,
  stat_record VARCHAR(32) NOT NULL,
  date_record date,
  id_event INT DEFAULT NULL,
  id_athlete INT DEFAULT NULL,
  CONSTRAINT fk_record_event FOREIGN KEY (id_event) REFERENCES Event (id_event) ON DELETE CASCADE,
  CONSTRAINT fk_record_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete (id_athlete) ON DELETE SET NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Transport
--

DROP TABLE IF EXISTS Transport;
CREATE TABLE Transport (
  id_trans SERIAL PRIMARY KEY,
  name_trans VARCHAR(8) NOT NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Site
--

DROP TABLE IF EXISTS Site;
CREATE TABLE Site (
  id_site SERIAL PRIMARY KEY,
  name_site VARCHAR(50) NOT NULL,
  adress_site VARCHAR(50) NOT NULL,
  creation_date_site date DEFAULT NULL,
  capacity_site INT DEFAULT NULL,
  URL_site VARCHAR(255) DEFAULT NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Team
--

DROP TABLE IF EXISTS Team;
CREATE TABLE Team (
  id_team SERIAL PRIMARY KEY,
  size_team INT NOT NULL,
  gender_team VARCHAR(6) NOT NULL,
  code_country char(3) DEFAULT NULL,
  CONSTRAINT fk_team_country FOREIGN KEY (code_country) REFERENCES Country (code_country) ON DELETE SET NULL
);

-- --------------------------------------------------------

--
-- Structure de la table Is_from
--

DROP TABLE IF EXISTS Is_from;
CREATE TABLE Is_from (
  id_athlete INT NOT NULL,
  code_country char(3) NOT NULL,
  PRIMARY KEY (id_athlete, code_country),
  CONSTRAINT fk_is_from_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete (id_athlete) ON DELETE CASCADE,
  CONSTRAINT fk_is_from_country FOREIGN KEY (code_country) REFERENCES Country (code_country) ON DELETE CASCADE
);

-- --------------------------------------------------------

--
-- Structure de la table To_pertain_team
--

DROP TABLE IF EXISTS To_pertain_team;
CREATE TABLE To_pertain_team (
  id_athlete INT NOT NULL,
  id_team INT NOT NULL,
  PRIMARY KEY (id_athlete, id_team),
  CONSTRAINT fk_to_pertain_team_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete (id_athlete) ON DELETE CASCADE,
  CONSTRAINT fk_to_pertain_team_team FOREIGN KEY (id_team) REFERENCES Team (id_team) ON DELETE CASCADE
);

-- --------------------------------------------------------

--
-- Structure de la table To_Register_athlete
--

DROP TABLE IF EXISTS To_Register_athlete;
CREATE TABLE To_Register_athlete (
  id_event INT NOT NULL,
  id_athlete INT NOT NULL,
  PRIMARY KEY (id_event, id_athlete),
  CONSTRAINT fk_to_register_athlete_event FOREIGN KEY (id_event) REFERENCES Event (id_event) ON DELETE CASCADE,
  CONSTRAINT fk_to_register_athlete_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete (id_athlete) ON DELETE CASCADE
);

-- --------------------------------------------------------

--
-- Structure de la table To_Register_team
--

DROP TABLE IF EXISTS To_Register_team;
CREATE TABLE To_Register_team (
  id_event INT NOT NULL,
  id_team INT NOT NULL,
  PRIMARY KEY (id_event, id_team),
  CONSTRAINT fk_to_register_team_event FOREIGN KEY (id_event) REFERENCES Event (id_event) ON DELETE CASCADE,
  CONSTRAINT fk_to_register_team_team FOREIGN KEY (id_team) REFERENCES Team (id_team) ON DELETE CASCADE
);

-- --------------------------------------------------------

--
-- Structure de la table To_Schedule
--

DROP TABLE IF EXISTS To_Schedule;
CREATE TABLE To_Schedule (
  id_site INT NOT NULL,
  id_date_cal INT NOT NULL,
  id_event INT NOT NULL,
  PRIMARY KEY (id_site, id_date_cal, id_event),
  CONSTRAINT fk_to_schedule_site FOREIGN KEY (id_site) REFERENCES Site (id_site) ON DELETE CASCADE,
  CONSTRAINT fk_to_schedule_date_calendar FOREIGN KEY (id_date_cal) REFERENCES Date_calendar (id_date_cal) ON DELETE CASCADE,
  CONSTRAINT fk_to_schedule_event FOREIGN KEY (id_event) REFERENCES Event (id_event) ON DELETE CASCADE
);

-- --------------------------------------------------------

--
-- Structure de la table To_Serve
--

DROP TABLE IF EXISTS To_Serve;
CREATE TABLE To_Serve (
  id_site INT NOT NULL,
  id_trans INT NOT NULL,
  num_ligne VARCHAR(50) NOT NULL,
  station_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_site, id_trans),
  CONSTRAINT fk_to_serve_site FOREIGN KEY (id_site) REFERENCES Site (id_site) ON DELETE CASCADE,
  CONSTRAINT fk_to_serve_transport FOREIGN KEY (id_trans) REFERENCES Transport (id_trans) ON DELETE CASCADE
);
