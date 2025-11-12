-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 12, 2025
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
 /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
 /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 /*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_perkantoran`
--
CREATE DATABASE IF NOT EXISTS `db_perkantoran` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `db_perkantoran`;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--
CREATE TABLE `admin` (
  `username` VARCHAR(10) NOT NULL,
  `password` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `pegawai`
--
CREATE TABLE `pegawai` (
  `IDPegawai` VARCHAR(5) NOT NULL,
  `Nama` VARCHAR(40) NOT NULL,
  `Status` VARCHAR(20) NOT NULL,
  `Telp` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`IDPegawai`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `peralatan`
--
CREATE TABLE `peralatan` (
  `KodeAlat` VARCHAR(5) NOT NULL,
  `NamaAlat` VARCHAR(30) NOT NULL,
  `Jenis` VARCHAR(20) NOT NULL,
  `Jumlah` INT NOT NULL,
  `Kondisi` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`KodeAlat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Example data for table `pegawai`
--
INSERT INTO `pegawai` (`IDPegawai`, `Nama`, `Status`, `Telp`) VALUES
('P001', 'Budi Santoso', 'Tetap', '081234567890'),
('P002', 'Siti Aminah', 'Kontrak', '082233445566'),
('P003', 'Rudi Hartono', 'Magang', '083355779900');

--
-- Example data for table `admin`
--
INSERT INTO `admin` (`username`, `password`) VALUES
('admin', '12345');

--
-- Example data for table `peralatan`
--
INSERT INTO `peralatan` (`KodeAlat`, `NamaAlat`, `Jenis`, `Jumlah`, `Kondisi`) VALUES
('A001', 'Laptop Lenovo', 'Elektronik', 5, 'Baik'),
('A002', 'Printer Canon', 'Elektronik', 3, 'Baik'),
('A003', 'Proyektor Epson', 'Elektronik', 2, 'Baik');

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
 /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
 /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
