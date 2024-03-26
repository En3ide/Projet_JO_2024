SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;

--
-- Base de données : Projet_JO_2024
--

--
-- Structure de la table Athlete
--

DROP TABLE IF EXISTS Athlete;
CREATE TABLE Athlete (
  id_athlete int(11) PRIMARY KEY AUTO_INCREMENT,
  firstname_athlete VARCHAR(32) NOT NULL,
  name_athlete VARCHAR(32) NOT NULL,
  birthday_athlete date DEFAULT NULL,
  gender_athlete enum('MAN', 'WOMAN') NOT NULL,
  code_country char(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table Country
--

DROP TABLE IF EXISTS Country;
CREATE TABLE Country (
  code_country char(3) NOT NULL PRIMARY KEY,
  name_country VARCHAR(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table Date_calendar
--

DROP TABLE IF EXISTS Date_calendar;
CREATE TABLE Date_calendar (
  id_date_cal int(11) PRIMARY KEY AUTO_INCREMENT,
  date_cal date NOT NULL,
  medal_ceremony_date_cal tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table Discipline
--

DROP TABLE IF EXISTS Discipline;
CREATE TABLE Discipline (
  id_disc int(11) PRIMARY KEY AUTO_INCREMENT,
  name_fr_disc VARCHAR(32) NOT NULL,
  name_an_disc VARCHAR(32),
  category_disc enum('OLYMPIC', 'PARALYMPIC') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table Event
--

DROP TABLE IF EXISTS Event;
CREATE TABLE Event (
  id_event int(11) PRIMARY KEY AUTO_INCREMENT,
  name_event VARCHAR(32) NOT NULL,
  format_event enum('INDIVIDUAL', 'COLLECTIVE', 'HYBRIDE') NOT NULL,
  gender_event enum('MAN', 'WOMAN', 'MIXED') NOT NULL,
  id_disc int(11) NOT NULL,
  id_record int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table Medal
--

DROP TABLE IF EXISTS Medal;
CREATE TABLE Medal (
  id_medal int(11) PRIMARY KEY AUTO_INCREMENT,
  type_medal enum('GOLD','SILVER','BRONZE') NOT NULL,
  id_event int(11) NOT NULL,
  id_athlete int(11) DEFAULT NULL,
  id_date_cal int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table Record
--

DROP TABLE IF EXISTS Record;
CREATE TABLE Record (
  id_record int(11) PRIMARY KEY AUTO_INCREMENT,
  stat_record VARCHAR(32) NOT NULL,
  date_record date,
  id_event int(11) NOT NULL,
  id_athlete int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table Transport
--

DROP TABLE IF EXISTS Transport;
CREATE TABLE Transport (
  id_trans int(11) PRIMARY KEY AUTO_INCREMENT,
  name_trans VARCHAR(32) enum('TRAIN', 'TRAMWAY', 'BUS', 'METRO') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table Site
--

DROP TABLE IF EXISTS Site;
CREATE TABLE Site (
  id_site int(11) PRIMARY KEY AUTO_INCREMENT,
  name_site VARCHAR(32) NOT NULL,
  adress_site VARCHAR(32) NOT NULL,
  creation_date_site date DEFAULT NULL,
  capacity_site int(11) DEFAULT NULL,
  URL_site VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table Team
--

DROP TABLE IF EXISTS Team;
CREATE TABLE Team (
  id_team int(11) PRIMARY KEY AUTO_INCREMENT,
  size_team int(11) NOT NULL,
  gender_team enum('MAN', 'WOMAN', 'MIXED') NOT NULL,
  code_country char(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table Is_from
--

DROP TABLE IF EXISTS Is_from;
CREATE TABLE Is_from (
  id_athlete int(11) NOT NULL,
  code_country char(3) NOT NULL,
  PRIMARY KEY (id_athlete, code_country)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table To_pertain_team
--

DROP TABLE IF EXISTS To_pertain_team;
CREATE TABLE To_pertain_team (
  id_athlete int(11) NOT NULL,
  id_team int(11) NOT NULL,
  PRIMARY KEY (id_athlete, id_team)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table To_Register_athlete
--

DROP TABLE IF EXISTS To_Register_athlete;
CREATE TABLE To_Register_athlete (
  id_event int(11) NOT NULL,
  id_athlete int(11) NOT NULL,
  PRIMARY KEY (id_event, id_athlete)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table To_Register_team
--

DROP TABLE IF EXISTS To_Register_team;
CREATE TABLE To_Register_team (
  id_event int(11) NOT NULL,
  id_team int(11) NOT NULL,
  PRIMARY KEY (id_event, id_team)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table To_Schedule
--

DROP TABLE IF EXISTS To_Schedule;
CREATE TABLE To_Schedule (
  id_site int(11) NOT NULL,
  id_date_cal int(11) NOT NULL,
  id_event int(11) NOT NULL,
  PRIMARY KEY (id_site, id_date_cal, id_event)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table To_Serve
--

DROP TABLE IF EXISTS To_Serve;
CREATE TABLE To_Serve (
  id_site int(11) NOT NULL,
  id_trans int(11) NOT NULL,
  num_ligne VARCHAR(32) NOT NULL,
  station_name VARCHAR(32) NOT NULL,
  PRIMARY KEY (id_site, id_trans)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



--
-- Index et Contraintes pour la table Athlete
--
ALTER TABLE Athlete
  ADD INDEX IDX_Athlete_code_country (code_country),

  ADD CONSTRAINT FK_Athlete_code_country FOREIGN KEY (code_country) REFERENCES Country (code_country) ON DELETE SET NULL;

--
-- Index et Contraintes pour la table Event
--
ALTER TABLE Event
  ADD INDEX IDX_Event_id_disc (id_disc),
  ADD INDEX IDX_Event_id_record (id_record),

  ADD CONSTRAINT FK_Event_id_disc FOREIGN KEY (id_disc) REFERENCES Discipline (id_disc) ON DELETE CASCADE,
  ADD CONSTRAINT FK_Event_id_record FOREIGN KEY (id_record) REFERENCES Record (id_record) ON DELETE SET NULL;

--
-- Index et Contraintes pour la table Medal
--
ALTER TABLE Medal
  ADD INDEX IDX_Medal_id_event (id_event),
  ADD INDEX IDX_Medal_id_athlete (id_athlete),
  ADD INDEX IDX_Medal_id_date_cal (id_date_cal),

  ADD CONSTRAINT FK_Medal_id_event FOREIGN KEY (id_event) REFERENCES Event (id_event) ON DELETE CASCADE,
  ADD CONSTRAINT FK_Medal_id_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete (id_athlete) ON DELETE SET NULL,
  ADD CONSTRAINT FK_Medal_id_date_cal FOREIGN KEY (id_date_cal) REFERENCES Date_calendar (id_date_cal) ON DELETE SET NULL;

--
-- Indexet Contraintes pour la table Record
--
ALTER TABLE Record
  ADD INDEX IDX_Record_id_event (id_event),
  ADD INDEX IDX_Record_id_athlete (id_athlete),

  ADD CONSTRAINT FK_Record_id_event FOREIGN KEY (id_event) REFERENCES Event (id_event) ON DELETE CASCADE,
  ADD CONSTRAINT FK_Record_id_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete (id_athlete) ON DELETE SET NULL;

--
-- Index pour la table Team et Contraintes pour la table Team
--
ALTER TABLE Team
  ADD INDEX IDX_Team_code_country (code_country),

  ADD CONSTRAINT FK_Team_code_country FOREIGN KEY (code_country) REFERENCES Country (code_country) ON DELETE SET NULL;

--
-- Index et Contraintes pour la table Is_from
--
ALTER TABLE Is_from
  -- ADD INDEX IDX_Is_from_id_athlete (id_athlete),
  -- ADD INDEX IDX_Is_from_code_country (code_country),

  ADD CONSTRAINT FK_Is_from_id_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete (id_athlete) ON DELETE CASCADE,
  ADD CONSTRAINT FK_Is_from_code_country FOREIGN KEY (code_country) REFERENCES Country (code_country) ON DELETE CASCADE;

--
-- Index et Contraintes pour la table To_pertain_team
--
ALTER TABLE To_pertain_team
  -- ADD INDEX IDX_To_pertain_team_id_team (id_team),
  -- ADD INDEX IDX_To_pertain_team_id_athlete (id_athlete),

  ADD CONSTRAINT FK_To_pertain_team_id_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete (id_athlete) ON DELETE CASCADE,
  ADD CONSTRAINT FK_To_pertain_team_id_team FOREIGN KEY (id_team) REFERENCES Team (id_team) ON DELETE CASCADE;

--
-- Index et Contraintes pour la table To_Register_athlete
--
ALTER TABLE To_Register_athlete
  -- ADD INDEX IDX_To_Register_athlete_id_athlete (id_athlete),
  -- ADD INDEX IDX_To_Register_athlete_id_event (id_event),

  ADD CONSTRAINT FK_To_Register_athlete_id_athlete FOREIGN KEY (id_athlete) REFERENCES Athlete (id_athlete) ON DELETE CASCADE,
  ADD CONSTRAINT FK_To_Register_athlete_id_event FOREIGN KEY (id_event) REFERENCES Event (id_event) ON DELETE CASCADE;

--
-- Index et Contraintes pour la table To_Register_team
--
ALTER TABLE To_Register_team
  -- ADD INDEX IDX_To_Register_team_id_team (id_team),
  -- ADD INDEX IDX_To_Register_team_id_event (id_event),

  ADD CONSTRAINT FK_To_Register_team_id_event FOREIGN KEY (id_event) REFERENCES Event (id_event) ON DELETE CASCADE,
  ADD CONSTRAINT FK_To_Register_team_id_team FOREIGN KEY (id_team) REFERENCES Team (id_team) ON DELETE CASCADE;

--
-- Index et Contraintes pour la table To_Schedule
--
ALTER TABLE To_Schedule
  -- ADD INDEX IDX_To_Schedule_id_date_cal (id_date_cal),
  -- ADD INDEX IDX_To_Schedule_id_event (id_event),
  -- ADD INDEX IDX_To_Schedule_id_site (id_site),

  ADD CONSTRAINT FK_To_Schedule_id_date_cal FOREIGN KEY (id_date_cal) REFERENCES Date_calendar (id_date_cal) ON DELETE CASCADE,
  ADD CONSTRAINT FK_To_Schedule_id_event FOREIGN KEY (id_event) REFERENCES Event (id_event) ON DELETE CASCADE,
  ADD CONSTRAINT FK_To_Schedule_id_site FOREIGN KEY (id_site) REFERENCES Site (id_site) ON DELETE CASCADE;

--
-- Index et Contraintes pour la table To_Serve
--
ALTER TABLE To_Serve
  -- ADD INDEX IDX_To_Serve_id_trans (id_trans),
  -- ADD INDEX IDX_To_Serve_id_site (id_site),

  ADD CONSTRAINT FK_To_Serve_id_site FOREIGN KEY (id_site) REFERENCES Site (id_site) ON DELETE CASCADE,
  ADD CONSTRAINT FK_To_Serve_id_trans FOREIGN KEY (id_trans) REFERENCES Transport (id_trans) ON DELETE CASCADE;

COMMIT;