SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `Projet_JO_2024`
--

--
-- Structure de la table `Athlete`
--

CREATE TABLE `Athlete` (
  `id_athlete` int(11) NOT NULL,
  `name_athlete` char(32) NOT NULL,
  `firstname_athlete` char(32) NOT NULL,
  `birthday_athlete` date NOT NULL,
  `code_country` char(3) NOT NULL,
  `gender_athlete` enum('MAN','WOMAN') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Country`
--

CREATE TABLE `Country` (
  `code_country` char(3) NOT NULL,
  `Country_name` char(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Date_calendar`
--

CREATE TABLE `Date_calendar` (
  `id_date_cal` int(11) NOT NULL,
  `Date` date NOT NULL,
  `medal_ceremony_date_cal` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Discipline`
--

CREATE TABLE `Discipline` (
  `id_disc` int(11) NOT NULL,
  `category_disc` enum('Olympic', 'Paralympic') NOT NULL,
  `format_disc` enum('Individual', 'Collective', 'Hybride') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Event`
--

CREATE TABLE `Event` (
  `id_event` int(11) NOT NULL,
  `name_event` char(32) NOT NULL,
  `id_disc` int(11) NOT NULL,
  `gender_event` enum('MAN','WOMAN') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Is_from`
--

CREATE TABLE `Is_from` (
  `id_athlete` int(32) NOT NULL,
  `id_nationality` int(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Medal`
--

CREATE TABLE `Medal` (
  `Medal_id` int(11) NOT NULL,
  `Medal_type` enum('GOLD','SILVER','BRONZE') NOT NULL,
  `id_event` int(11) NOT NULL,
  `id_team` int(11),
  `id_athlete` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Nationality`
--

CREATE TABLE `Nationality` (
  `id_nationality` int(11) NOT NULL,
  `name_nationality` char(32) NOT NULL,
  `code_country` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Record`
--

CREATE TABLE `Record` (
  `id_record` int(11) NOT NULL,
  `stat_record` char(32) NOT NULL,
  `holder_record` int(11) NOT NULL,
  `date_record` date NOT NULL,
  `id_event` int(11) NOT NULL,
  `id_team` int(11),
  `id_athlete` int(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Site`
--

CREATE TABLE `Site` (
  `id_site` int(11) NOT NULL,
  `Creation_date_site` date,
  `adress_site` char(32) NOT NULL,
  `capacity_site` int(11) NOT NULL,
  `URL_site` char(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Team`
--

CREATE TABLE `Team` (
  `id_team` int(11) NOT NULL,
  `size_team` int(11) NOT NULL,
  `code_country` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `To_pertain_team`
--

CREATE TABLE `To_pertain_team` (
  `id_athlete` int(32) NOT NULL,
  `id_team` int(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `To_Register_athlete`
--

CREATE TABLE `To_Register_athlete` (
  `id_event` int(32) NOT NULL,
  `id_athlete` int(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `To_Register_team`
--

CREATE TABLE `To_Register_team` (
  `id_event` int(32) NOT NULL,
  `id_team` int(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `To_Schedule`
--

CREATE TABLE `To_Schedule` (
  `id_site` int(11) NOT NULL,
  `id_date_cal` int(11) NOT NULL,
  `id_event` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `To_Serve`
--

CREATE TABLE `To_Serve` (
  `id_site` int(11) NOT NULL,
  `id_trans` int(11) NOT NULL,
  `num_ligne` char(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Transport`
--

CREATE TABLE `Transport` (
  `name_trans` char(32) NOT NULL,
  `id_trans` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Athlete`
--
ALTER TABLE `Athlete`
  ADD PRIMARY KEY (`id_athlete`),
  ADD KEY `FK_Athlete_Country_code` (`code_country`);

--
-- Index pour la table `Country`
--
ALTER TABLE `Country`
  ADD PRIMARY KEY (`code_country`);

--
-- Index pour la table `Date_calendar`
--
ALTER TABLE `Date_calendar`
  ADD PRIMARY KEY (`id_date_cal`);

--
-- Index pour la table `Discipline`
--
ALTER TABLE `Discipline`
  ADD PRIMARY KEY (`id_disc`),
  ADD KEY `FK_Discipline_Date_start` (`Date_start`),
  ADD KEY `FK_Discipline_Date_end` (`Date_end`);

--
-- Index pour la table `Event`
--
ALTER TABLE `Event`
  ADD PRIMARY KEY (`id_event`),
  ADD KEY `FK_id_event_disc` (`id_disc`);

--
-- Index pour la table `Is_from`
--
ALTER TABLE `Is_from`
  ADD PRIMARY KEY (`id_athlete`,`id_nationality`),
  ADD KEY `FK_Is_from_id_nationality` (`id_nationality`);

--
-- Index pour la table `Medal`
--
ALTER TABLE `Medal`
  ADD PRIMARY KEY (`Medal_id`),
  ADD KEY `FK_Medal_id_event` (`id_event`);

--
-- Index pour la table `Nationality`
--
ALTER TABLE `Nationality`
  ADD PRIMARY KEY (`id_nationality`);

--
-- Index pour la table `Record`
--
ALTER TABLE `Record`
  ADD PRIMARY KEY (`id_record`),
  ADD KEY `FK_id_record_event` (`id_event`),
  ADD KEY `FK_id_record_team`;

--
-- Index pour la table `Site`
--
ALTER TABLE `Site`
  ADD PRIMARY KEY (`id_site`);

--
-- Index pour la table `Team`
--
ALTER TABLE `Team`
  ADD PRIMARY KEY (`id_team`),
  ADD KEY `FK_Team_Country_code` (`code_country`);

--
-- Index pour la table `To_pertain_team`
--
ALTER TABLE `To_pertain_team`
  ADD PRIMARY KEY (`id_athlete`,`id_team`),
  ADD KEY `FK_To_pertain_team_id_team` (`id_team`);

--
-- Index pour la table `To_Register_athlete`
--
ALTER TABLE `To_Register_athlete`
  ADD PRIMARY KEY (`id_event`,`id_athlete`),
  ADD KEY `FK_To_Register_athlete_id_athlete` (`id_athlete`);

--
-- Index pour la table `To_Register_team`
--
ALTER TABLE `To_Register_team`
  ADD PRIMARY KEY (`id_event`,`id_team`),
  ADD KEY `FK_To_Register_team_id_team` (`id_team`);

--
-- Index pour la table `To_Schedule`
--
ALTER TABLE `To_Schedule`
  ADD PRIMARY KEY (`id_site`,`id_date_cal`,`id_event`),
  ADD KEY `FK_To_Schedule_id_date_cal` (`id_date_cal`),
  ADD KEY `FK_To_Schedule_id_event` (`id_event`);

--
-- Index pour la table `To_Serve`
--
ALTER TABLE `To_Serve`
  ADD PRIMARY KEY (`id_site`,`id_trans`),
  ADD KEY `FK_To_Serve_id_trans` (`id_trans`);

--
-- Index pour la table `Transport`
--
ALTER TABLE `Transport`
  ADD PRIMARY KEY (`id_trans`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `Athlete`
--
ALTER TABLE `Athlete`
  MODIFY `id_athlete` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Date_calendar`
--
ALTER TABLE `Date_calendar`
  MODIFY `id_date_cal` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Discipline`
--
ALTER TABLE `Discipline`
  MODIFY `id_disc` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Event`
--
ALTER TABLE `Event`
  MODIFY `id_event` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Medal`
--
ALTER TABLE `Medal`
  MODIFY `Medal_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Nationality`
--
ALTER TABLE `Nationality`
  MODIFY `id_nationality` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Record`
--
ALTER TABLE `Record`
  MODIFY `id_record` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Site`
--
ALTER TABLE `Site`
  MODIFY `id_site` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Team`
--
ALTER TABLE `Team`
  MODIFY `id_team` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Transport`
--
ALTER TABLE `Transport`
  MODIFY `id_trans` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

ALTER TABLE `Nationality`
  ADD CONSTRAINT `FK_Nationality_code_country` FOREIGN KEY (`code_country`) REFERENCES `Country` (`code_country`);

--
-- Contraintes pour la table `Athlete`
--
ALTER TABLE `Athlete`
  ADD CONSTRAINT `FK_Athlete_code_country` FOREIGN KEY (`code_country`) REFERENCES `Country` (`code_country`);

--
-- Contraintes pour la table `Discipline`
--
ALTER TABLE `Discipline`
  ADD CONSTRAINT `FK_Discipline_Date_end` FOREIGN KEY (`Date_end`) REFERENCES `Date_calendar` (`id_date_cal`),
  ADD CONSTRAINT `FK_Discipline_Date_start` FOREIGN KEY (`Date_start`) REFERENCES `Date_calendar` (`id_date_cal`);

--
-- Contraintes pour la table `Event`
--
ALTER TABLE `Event`
  ADD CONSTRAINT `FK_id_event_disc` FOREIGN KEY (`id_disc`) REFERENCES `Discipline` (`id_disc`);

--
-- Contraintes pour la table `Is_from`
--
ALTER TABLE `Is_from`
  ADD CONSTRAINT `FK_Is_from_id_athlete` FOREIGN KEY (`id_athlete`) REFERENCES `Athlete` (`id_athlete`),
  ADD CONSTRAINT `FK_Is_from_id_nationality` FOREIGN KEY (`id_nationality`) REFERENCES `Nationality` (`id_nationality`);

--
-- Contraintes pour la table `Medal`
--
ALTER TABLE `Medal`
  ADD CONSTRAINT `FK_Medal_id_event` FOREIGN KEY (`id_event`) REFERENCES `Event` (`id_event`),
  ADD CONSTRAINT `FK_Medal_id_athlete` FOREIGN KEY (`id_athlete`) REFERENCES `Athlete` (`id_athlete`),
  ADD CONSTRAINT `FK_Medal_id_team` FOREIGN KEY (`id_team`) REFERENCES `Team` (`id_team`);
--
-- Contraintes pour la table `Nationality`
--
ALTER TABLE `Nationality`
  ADD CONSTRAINT `Nationality_ibfk_1` FOREIGN KEY (`id_nationality`) REFERENCES `Athlete` (`id_athlete`);

--
-- Contraintes pour la table `Record`
--
ALTER TABLE `Record`
  ADD CONSTRAINT `FK_id_record_event` FOREIGN KEY (`id_event`) REFERENCES `Event` (`id_event`),
  ADD CONSTRAINT `FK_record_id_team` FOREIGN KEY (`id_team`) REFERENCES `Team` (`id_team`),
  ADD CONSTRAINT `FK_record_id_athlete` FOREIGN KEY (`id_athlete`) REFERENCES `Athlete` (`id_athlete`);

--
-- Contraintes pour la table `Team`
--
ALTER TABLE `Team`
  ADD CONSTRAINT `FK_Team_Country_code` FOREIGN KEY (`code_country`) REFERENCES `Country` (`code_country`);

--
-- Contraintes pour la table `To_pertain_team`
--
ALTER TABLE `To_pertain_team`
  ADD CONSTRAINT `FK_To_pertain_id_team_athlete` FOREIGN KEY (`id_athlete`) REFERENCES `Athlete` (`id_athlete`),
  ADD CONSTRAINT `FK_To_pertain_team_id_team` FOREIGN KEY (`id_team`) REFERENCES `Team` (`id_team`);

--
-- Contraintes pour la table `To_Register_athlete`
--
ALTER TABLE `To_Register_athlete`
  ADD CONSTRAINT `FK_To_Register_athlete_id_athlete` FOREIGN KEY (`id_athlete`) REFERENCES `Athlete` (`id_athlete`),
  ADD CONSTRAINT `FK_To_Register_athlete_id_event` FOREIGN KEY (`id_event`) REFERENCES `Event` (`id_event`);

--
-- Contraintes pour la table `To_Register_team`
--
ALTER TABLE `To_Register_team`
  ADD CONSTRAINT `FK_To_Register_team_id_event` FOREIGN KEY (`id_event`) REFERENCES `Event` (`id_event`),
  ADD CONSTRAINT `FK_To_Register_team_id_team` FOREIGN KEY (`id_team`) REFERENCES `Team` (`id_team`);

--
-- Contraintes pour la table `To_Schedule`
--
ALTER TABLE `To_Schedule`
  ADD CONSTRAINT `FK_To_Schedule_id_date_cal` FOREIGN KEY (`id_date_cal`) REFERENCES `Date_calendar` (`id_date_cal`),
  ADD CONSTRAINT `FK_To_Schedule_id_event` FOREIGN KEY (`id_event`) REFERENCES `Event` (`id_event`),
  ADD CONSTRAINT `FK_To_Schedule_id_site` FOREIGN KEY (`id_site`) REFERENCES `Site` (`id_site`);

--
-- Contraintes pour la table `To_Serve`
--
ALTER TABLE `To_Serve`
  ADD CONSTRAINT `FK_To_Serve_id_site` FOREIGN KEY (`id_site`) REFERENCES `Site` (`id_site`),
  ADD CONSTRAINT `FK_To_Serve_id_trans` FOREIGN KEY (`id_trans`) REFERENCES `Transport` (`id_trans`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
