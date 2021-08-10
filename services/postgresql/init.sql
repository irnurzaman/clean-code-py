--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

-- Started on 2021-08-10 11:54:16

--
-- TOC entry 3004 (class 1262 OID 33333)
-- Name: bds; Type: DATABASE; Schema: -; Owner: bds
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 200 (class 1259 OID 33334)
-- Name: nasabah; Type: TABLE; Schema: public; Owner: bds
--

CREATE TABLE public.nasabah (
    cif text NOT NULL,
    ktp text NOT NULL,
    nama text NOT NULL,
    pekerjaan text NOT NULL,
    alamat text NOT NULL
);


ALTER TABLE public.nasabah OWNER TO bds;

--
-- TOC entry 201 (class 1259 OID 33342)
-- Name: rekening; Type: TABLE; Schema: public; Owner: bds
--

CREATE TABLE public.rekening (
    no_rekening text NOT NULL,
    saldo double precision NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);


ALTER TABLE public.rekening OWNER TO bds;

--
-- TOC entry 202 (class 1259 OID 33351)
-- Name: rekening_nasabah; Type: TABLE; Schema: public; Owner: bds
--

CREATE TABLE public.rekening_nasabah (
    cif text NOT NULL,
    no_rekening text NOT NULL
);


ALTER TABLE public.rekening_nasabah OWNER TO bds;

--
-- TOC entry 2861 (class 2606 OID 33341)
-- Name: nasabah nasabah_pkey; Type: CONSTRAINT; Schema: public; Owner: bds
--

ALTER TABLE ONLY public.nasabah
    ADD CONSTRAINT nasabah_pkey PRIMARY KEY (cif);


--
-- TOC entry 2863 (class 2606 OID 33350)
-- Name: rekening rekening_pkey; Type: CONSTRAINT; Schema: public; Owner: bds
--

ALTER TABLE ONLY public.rekening
    ADD CONSTRAINT rekening_pkey PRIMARY KEY (no_rekening);


--
-- TOC entry 2864 (class 2606 OID 33357)
-- Name: rekening_nasabah nasabah_fk; Type: FK CONSTRAINT; Schema: public; Owner: bds
--

ALTER TABLE ONLY public.rekening_nasabah
    ADD CONSTRAINT nasabah_fk FOREIGN KEY (cif) REFERENCES public.nasabah(cif);


--
-- TOC entry 2865 (class 2606 OID 33362)
-- Name: rekening_nasabah rekening_fk; Type: FK CONSTRAINT; Schema: public; Owner: bds
--

ALTER TABLE ONLY public.rekening_nasabah
    ADD CONSTRAINT rekening_fk FOREIGN KEY (no_rekening) REFERENCES public.rekening(no_rekening);


-- Completed on 2021-08-10 11:54:18

--
-- PostgreSQL database dump complete
--

