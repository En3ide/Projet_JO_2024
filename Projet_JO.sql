SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `Projet_JO`
--

--
-- Structure de la table `Athlete`
--

CREATE TABLE `Athlete` (
  `Athlete_id` int(11) NOT NULL,
  `Athlete_name` char(32) NOT NULL,
  `Athlete_firstName` int(32) NOT NULL,
  `Athlete_birthday` date NOT NULL,
  `Country_code` char(3) NOT NULL,
  `Athlete_gender` enum('MAN','WOMAN') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Country`
--

CREATE TABLE `Country` (
  `Country_code` char(3) NOT NULL,
  `Country_name` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Date_calendar`
--

CREATE TABLE `Date_calendar` (
  `Date_id` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Medal_ceremony` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Discipline`
--

CREATE TABLE `Discipline` (
  `Discipline_id` int(11) NOT NULL,
  `Category` char(32) NOT NULL,
  `Format_Discipline` char(32) NOT NULL,
  `Date_start` int(11) NOT NULL,
  `Date_end` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Event`
--

CREATE TABLE `Event` (
  `Event_id` int(11) NOT NULL,
  `Event_name` char(32) NOT NULL,
  `Discipline_id` int(11) NOT NULL,
  `Event_gender` enum('MAN','WOMAN') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Is_from`
--

CREATE TABLE `Is_from` (
  `Athlete_id` int(32) NOT NULL,
  `Nationality_id` int(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Medal`
--

CREATE TABLE `Medal` (
  `Medal_id` int(11) NOT NULL,
  `Medal_type` enum('GOLD','SILVER','BRONZE') NOT NULL,
  `Event_id` int(11) NOT NULL,
  `Team_id` int(11),
  `Athlete_id` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Nationality`
--

CREATE TABLE `Nationality` (
  `Nationality_id` int(11) NOT NULL,
  `Nationality_name` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Record`
--

CREATE TABLE `Record` (
  `Record_id` int(11) NOT NULL,
  `Record_stat` char(32) NOT NULL,
  `Record_holder` int(11) NOT NULL,
  `Record_date` date NOT NULL,
  `Event_id` int(11) NOT NULL,
  `Team_id` int(11),
  `Athlete` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Site`
--

CREATE TABLE `Site` (
  `Site_id` int(11) NOT NULL,
  `Creation_date` date NOT NULL,
  `Adress` char(32) NOT NULL,
  `Capacity` int(11) NOT NULL,
  `URL_site` char(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Team`
--

CREATE TABLE `Team` (
  `Team_id` int(11) NOT NULL,
  `Team_size` int(11) NOT NULL,
  `Country_code` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `To_pertain_team`
--

CREATE TABLE `To_pertain_team` (
  `Athlete_id` int(32) NOT NULL,
  `Team_id` int(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `To_Register_athlete`
--

CREATE TABLE `To_Register_athlete` (
  `Event_id` int(32) NOT NULL,
  `Athlete_id` int(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `To_Register_team`
--

CREATE TABLE `To_Register_team` (
  `Event_id` int(32) NOT NULL,
  `Team_id` int(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `To_Schedule`
--

CREATE TABLE `To_Schedule` (
  `Site_id` int(11) NOT NULL,
  `Date_id` int(11) NOT NULL,
  `Event_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `To_Serve`
--

CREATE TABLE `To_Serve` (
  `Site_id` int(11) NOT NULL,
  `Transport_id` int(11) NOT NULL,
  `Num_ligne` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Transport`
--

CREATE TABLE `Transport` (
  `Transport_name` char(32) NOT NULL,
  `Transport_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Athlete`
--
ALTER TABLE `Athlete`
  ADD PRIMARY KEY (`Athlete_id`),
  ADD KEY `FK_Athlete_Country_code` (`Country_code`);

--
-- Index pour la table `Country`
--
ALTER TABLE `Country`
  ADD PRIMARY KEY (`Country_code`);

--
-- Index pour la table `Date_calendar`
--
ALTER TABLE `Date_calendar`
  ADD PRIMARY KEY (`Date_id`);

--
-- Index pour la table `Discipline`
--
ALTER TABLE `Discipline`
  ADD PRIMARY KEY (`Discipline_id`),
  ADD KEY `FK_Discipline_Date_start` (`Date_start`),
  ADD KEY `FK_Discipline_Date_end` (`Date_end`);

--
-- Index pour la table `Event`
--
ALTER TABLE `Event`
  ADD PRIMARY KEY (`Event_id`),
  ADD KEY `FK_Event_Discipline_id` (`Discipline_id`);

--
-- Index pour la table `Is_from`
--
ALTER TABLE `Is_from`
  ADD PRIMARY KEY (`Athlete_id`,`Nationality_id`),
  ADD KEY `FK_Is_from_Nationality_id` (`Nationality_id`);

--
-- Index pour la table `Medal`
--
ALTER TABLE `Medal`
  ADD PRIMARY KEY (`Medal_id`),
  ADD KEY `FK_Medal_Event_id` (`Event_id`);

--
-- Index pour la table `Nationality`
--
ALTER TABLE `Nationality`
  ADD PRIMARY KEY (`Nationality_id`);

--
-- Index pour la table `Record`
--
ALTER TABLE `Record`
  ADD PRIMARY KEY (`Record_id`),
  ADD KEY `FK_Record_Event_id` (`Event_id`);

--
-- Index pour la table `Site`
--
ALTER TABLE `Site`
  ADD PRIMARY KEY (`Site_id`);

--
-- Index pour la table `Team`
--
ALTER TABLE `Team`
  ADD PRIMARY KEY (`Team_id`),
  ADD KEY `FK_Team_Country_code` (`Country_code`);

--
-- Index pour la table `To_pertain_team`
--
ALTER TABLE `To_pertain_team`
  ADD PRIMARY KEY (`Athlete_id`,`Team_id`),
  ADD KEY `FK_To_pertain_team_Team_id` (`Team_id`);

--
-- Index pour la table `To_Register_athlete`
--
ALTER TABLE `To_Register_athlete`
  ADD PRIMARY KEY (`Event_id`,`Athlete_id`),
  ADD KEY `FK_To_Register_athlete_Athlete_id` (`Athlete_id`);

--
-- Index pour la table `To_Register_team`
--
ALTER TABLE `To_Register_team`
  ADD PRIMARY KEY (`Event_id`,`Team_id`),
  ADD KEY `FK_To_Register_team_Team_id` (`Team_id`);

--
-- Index pour la table `To_Schedule`
--
ALTER TABLE `To_Schedule`
  ADD PRIMARY KEY (`Site_id`,`Date_id`,`Event_id`),
  ADD KEY `FK_To_Schedule_Date_id` (`Date_id`),
  ADD KEY `FK_To_Schedule_Event_id` (`Event_id`);

--
-- Index pour la table `To_Serve`
--
ALTER TABLE `To_Serve`
  ADD PRIMARY KEY (`Site_id`,`Transport_id`),
  ADD KEY `FK_To_Serve_Transport_id` (`Transport_id`);

--
-- Index pour la table `Transport`
--
ALTER TABLE `Transport`
  ADD PRIMARY KEY (`Transport_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `Athlete`
--
ALTER TABLE `Athlete`
  MODIFY `Athlete_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Date_calendar`
--
ALTER TABLE `Date_calendar`
  MODIFY `Date_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Discipline`
--
ALTER TABLE `Discipline`
  MODIFY `Discipline_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Event`
--
ALTER TABLE `Event`
  MODIFY `Event_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Medal`
--
ALTER TABLE `Medal`
  MODIFY `Medal_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Nationality`
--
ALTER TABLE `Nationality`
  MODIFY `Nationality_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Record`
--
ALTER TABLE `Record`
  MODIFY `Record_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Site`
--
ALTER TABLE `Site`
  MODIFY `Site_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Team`
--
ALTER TABLE `Team`
  MODIFY `Team_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Transport`
--
ALTER TABLE `Transport`
  MODIFY `Transport_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `Athlete`
--
ALTER TABLE `Athlete`
  ADD CONSTRAINT `FK_Athlete_Country_code` FOREIGN KEY (`Country_code`) REFERENCES `Country` (`Country_code`);

--
-- Contraintes pour la table `Discipline`
--
ALTER TABLE `Discipline`
  ADD CONSTRAINT `FK_Discipline_Date_end` FOREIGN KEY (`Date_end`) REFERENCES `Date_calendar` (`Date_id`),
  ADD CONSTRAINT `FK_Discipline_Date_start` FOREIGN KEY (`Date_start`) REFERENCES `Date_calendar` (`Date_id`);

--
-- Contraintes pour la table `Event`
--
ALTER TABLE `Event`
  ADD CONSTRAINT `FK_Event_Discipline_id` FOREIGN KEY (`Discipline_id`) REFERENCES `Discipline` (`Discipline_id`);

--
-- Contraintes pour la table `Is_from`
--
ALTER TABLE `Is_from`
  ADD CONSTRAINT `FK_Is_from_Athlete_id` FOREIGN KEY (`Athlete_id`) REFERENCES `Athlete` (`Athlete_id`),
  ADD CONSTRAINT `FK_Is_from_Nationality_id` FOREIGN KEY (`Nationality_id`) REFERENCES `Nationality` (`Nationality_id`);

--
-- Contraintes pour la table `Medal`
--
ALTER TABLE `Medal`
  ADD CONSTRAINT `FK_Medal_Event_id` FOREIGN KEY (`Event_id`) REFERENCES `Event` (`Event_id`);

--
-- Contraintes pour la table `Nationality`
--
ALTER TABLE `Nationality`
  ADD CONSTRAINT `Nationality_ibfk_1` FOREIGN KEY (`Nationality_id`) REFERENCES `Athlete` (`Athlete_id`);

--
-- Contraintes pour la table `Record`
--
ALTER TABLE `Record`
  ADD CONSTRAINT `FK_Record_Event_id` FOREIGN KEY (`Event_id`) REFERENCES `Event` (`Event_id`);

--
-- Contraintes pour la table `Team`
--
ALTER TABLE `Team`
  ADD CONSTRAINT `FK_Team_Country_code` FOREIGN KEY (`Country_code`) REFERENCES `Country` (`Country_code`);

--
-- Contraintes pour la table `To_pertain_team`
--
ALTER TABLE `To_pertain_team`
  ADD CONSTRAINT `FK_To_pertain_team_Athlete_id` FOREIGN KEY (`Athlete_id`) REFERENCES `Athlete` (`Athlete_id`),
  ADD CONSTRAINT `FK_To_pertain_team_Team_id` FOREIGN KEY (`Team_id`) REFERENCES `Team` (`Team_id`);

--
-- Contraintes pour la table `To_Register_athlete`
--
ALTER TABLE `To_Register_athlete`
  ADD CONSTRAINT `FK_To_Register_athlete_Athlete_id` FOREIGN KEY (`Athlete_id`) REFERENCES `Athlete` (`Athlete_id`),
  ADD CONSTRAINT `FK_To_Register_athlete_Event_id` FOREIGN KEY (`Event_id`) REFERENCES `Event` (`Event_id`);

--
-- Contraintes pour la table `To_Register_team`
--
ALTER TABLE `To_Register_team`
  ADD CONSTRAINT `FK_To_Register_team_Event_id` FOREIGN KEY (`Event_id`) REFERENCES `Event` (`Event_id`),
  ADD CONSTRAINT `FK_To_Register_team_Team_id` FOREIGN KEY (`Team_id`) REFERENCES `Team` (`Team_id`);

--
-- Contraintes pour la table `To_Schedule`
--
ALTER TABLE `To_Schedule`
  ADD CONSTRAINT `FK_To_Schedule_Date_id` FOREIGN KEY (`Date_id`) REFERENCES `Date_calendar` (`Date_id`),
  ADD CONSTRAINT `FK_To_Schedule_Event_id` FOREIGN KEY (`Event_id`) REFERENCES `Event` (`Event_id`),
  ADD CONSTRAINT `FK_To_Schedule_Site_id` FOREIGN KEY (`Site_id`) REFERENCES `Site` (`Site_id`);

--
-- Contraintes pour la table `To_Serve`
--
ALTER TABLE `To_Serve`
  ADD CONSTRAINT `FK_To_Serve_Site_id` FOREIGN KEY (`Site_id`) REFERENCES `Site` (`Site_id`),
  ADD CONSTRAINT `FK_To_Serve_Transport_id` FOREIGN KEY (`Transport_id`) REFERENCES `Transport` (`Transport_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
