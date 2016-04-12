--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.11
-- Dumped by pg_dump version 9.4.6
-- Started on 2016-03-24 14:31:58 BRT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 2926 (class 1262 OID 16388)
-- Name: securities_master; Type: DATABASE; Schema: -; Owner: -
--



SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 8 (class 2615 OID 16782)
-- Name: securities; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA IF NOT EXISTS securities;


--
-- TOC entry 1 (class 3079 OID 12702)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2928 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = securities, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 179 (class 1259 OID 16834)
-- Name: daily_price; Type: TABLE; Schema: securities; Owner: -; Tablespace:
--

CREATE TABLE daily_price (
    id integer NOT NULL,
    data_vendor_id integer NOT NULL,
    symbol_id integer NOT NULL,
    price_date timestamp without time zone NOT NULL,
    created_date timestamp without time zone NOT NULL,
    last_updated_date timestamp without time zone NOT NULL,
    open_price numeric(19,4),
    high_price numeric(19,4),
    low_price numeric(19,4),
    close_price numeric(19,4),
    adj_close_price numeric(19,10),
    volume bigint
);


--
-- TOC entry 178 (class 1259 OID 16832)
-- Name: daily_price_id_seq; Type: SEQUENCE; Schema: securities; Owner: -
--

CREATE SEQUENCE daily_price_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2929 (class 0 OID 0)
-- Dependencies: 178
-- Name: daily_price_id_seq; Type: SEQUENCE OWNED BY; Schema: securities; Owner: -
--

ALTER SEQUENCE daily_price_id_seq OWNED BY daily_price.id;


--
-- TOC entry 175 (class 1259 OID 16796)
-- Name: data_vendor; Type: TABLE; Schema: securities; Owner: -; Tablespace:
--

CREATE TABLE data_vendor (
    id integer NOT NULL,
    name character varying(64) NOT NULL,
    website_url character varying(255),
    support_email character varying(255),
    created_date timestamp without time zone NOT NULL,
    last_updated_date timestamp without time zone NOT NULL
);


--
-- TOC entry 174 (class 1259 OID 16794)
-- Name: data_vendor_id_seq; Type: SEQUENCE; Schema: securities; Owner: -
--

CREATE SEQUENCE data_vendor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2930 (class 0 OID 0)
-- Dependencies: 174
-- Name: data_vendor_id_seq; Type: SEQUENCE OWNED BY; Schema: securities; Owner: -
--

ALTER SEQUENCE data_vendor_id_seq OWNED BY data_vendor.id;


--
-- TOC entry 173 (class 1259 OID 16785)
-- Name: exchange; Type: TABLE; Schema: securities; Owner: -; Tablespace:
--

CREATE TABLE exchange (
    id integer NOT NULL,
    abbrev character varying(32) NOT NULL,
    name character varying(255) NOT NULL,
    city character varying(255),
    country character varying(255),
    currency character varying(64),
    timezone_offset time without time zone,
    created_date timestamp without time zone NOT NULL,
    last_updated_date timestamp without time zone NOT NULL
);


--
-- TOC entry 172 (class 1259 OID 16783)
-- Name: exchange_id_seq; Type: SEQUENCE; Schema: securities; Owner: -
--

CREATE SEQUENCE exchange_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2931 (class 0 OID 0)
-- Dependencies: 172
-- Name: exchange_id_seq; Type: SEQUENCE OWNED BY; Schema: securities; Owner: -
--

ALTER SEQUENCE exchange_id_seq OWNED BY exchange.id;


--
-- TOC entry 177 (class 1259 OID 16818)
-- Name: symbol; Type: TABLE; Schema: securities; Owner: -; Tablespace:
--

CREATE TABLE symbol (
    id integer NOT NULL,
    exchange_id integer,
    ticker character varying(32) NOT NULL,
    instrument character varying(64) NOT NULL,
    name character varying(255),
    sector character varying(255),
    currency character varying(32),
    created_date timestamp without time zone NOT NULL,
    last_updated_date timestamp without time zone NOT NULL
);


--
-- TOC entry 176 (class 1259 OID 16816)
-- Name: symbol_id_seq; Type: SEQUENCE; Schema: securities; Owner: -
--

CREATE SEQUENCE symbol_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2932 (class 0 OID 0)
-- Dependencies: 176
-- Name: symbol_id_seq; Type: SEQUENCE OWNED BY; Schema: securities; Owner: -
--

ALTER SEQUENCE symbol_id_seq OWNED BY symbol.id;


--
-- TOC entry 2799 (class 2604 OID 16837)
-- Name: id; Type: DEFAULT; Schema: securities; Owner: -
--

ALTER TABLE ONLY daily_price ALTER COLUMN id SET DEFAULT nextval('daily_price_id_seq'::regclass);


--
-- TOC entry 2797 (class 2604 OID 16799)
-- Name: id; Type: DEFAULT; Schema: securities; Owner: -
--

ALTER TABLE ONLY data_vendor ALTER COLUMN id SET DEFAULT nextval('data_vendor_id_seq'::regclass);


--
-- TOC entry 2796 (class 2604 OID 16788)
-- Name: id; Type: DEFAULT; Schema: securities; Owner: -
--

ALTER TABLE ONLY exchange ALTER COLUMN id SET DEFAULT nextval('exchange_id_seq'::regclass);


--
-- TOC entry 2798 (class 2604 OID 16821)
-- Name: id; Type: DEFAULT; Schema: securities; Owner: -
--

ALTER TABLE ONLY symbol ALTER COLUMN id SET DEFAULT nextval('symbol_id_seq'::regclass);


--
-- TOC entry 2810 (class 2606 OID 16839)
-- Name: daily_price_pkey; Type: CONSTRAINT; Schema: securities; Owner: -; Tablespace:
--

ALTER TABLE ONLY daily_price
    ADD CONSTRAINT daily_price_pkey PRIMARY KEY (id);


--
-- TOC entry 2805 (class 2606 OID 16804)
-- Name: data_vendor_pkey; Type: CONSTRAINT; Schema: securities; Owner: -; Tablespace:
--

ALTER TABLE ONLY data_vendor
    ADD CONSTRAINT data_vendor_pkey PRIMARY KEY (id);


--
-- TOC entry 2802 (class 2606 OID 16793)
-- Name: exchange_pkey; Type: CONSTRAINT; Schema: securities; Owner: -; Tablespace:
--

ALTER TABLE ONLY exchange
    ADD CONSTRAINT exchange_pkey PRIMARY KEY (id);


--
-- TOC entry 2808 (class 2606 OID 16826)
-- Name: symbol_pkey; Type: CONSTRAINT; Schema: securities; Owner: -; Tablespace:
--

ALTER TABLE ONLY symbol
    ADD CONSTRAINT symbol_pkey PRIMARY KEY (id);


--
-- TOC entry 2811 (class 1259 OID 16850)
-- Name: daily_price_symbol_id_idx; Type: INDEX; Schema: securities; Owner: -; Tablespace:
--

CREATE INDEX daily_price_symbol_id_idx ON daily_price USING btree (symbol_id);


--
-- TOC entry 2803 (class 1259 OID 16853)
-- Name: data_vendor_id_idx; Type: INDEX; Schema: securities; Owner: -; Tablespace:
--

CREATE INDEX data_vendor_id_idx ON data_vendor USING btree (id);


--
-- TOC entry 2800 (class 1259 OID 16852)
-- Name: exchange_id_idx; Type: INDEX; Schema: securities; Owner: -; Tablespace:
--

CREATE INDEX exchange_id_idx ON exchange USING btree (id);


--
-- TOC entry 2806 (class 1259 OID 16851)
-- Name: symbol_id_idx; Type: INDEX; Schema: securities; Owner: -; Tablespace:
--

CREATE INDEX symbol_id_idx ON symbol USING btree (id);


--
-- TOC entry 2813 (class 2606 OID 16840)
-- Name: daily_price_data_vendor_id_fkey; Type: FK CONSTRAINT; Schema: securities; Owner: -
--

ALTER TABLE ONLY daily_price
    ADD CONSTRAINT daily_price_data_vendor_id_fkey FOREIGN KEY (data_vendor_id) REFERENCES data_vendor(id);


--
-- TOC entry 2814 (class 2606 OID 16845)
-- Name: daily_price_symbol_id_fkey; Type: FK CONSTRAINT; Schema: securities; Owner: -
--

ALTER TABLE ONLY daily_price
    ADD CONSTRAINT daily_price_symbol_id_fkey FOREIGN KEY (symbol_id) REFERENCES symbol(id);


--
-- TOC entry 2812 (class 2606 OID 16827)
-- Name: symbol_exchange_id_fkey; Type: FK CONSTRAINT; Schema: securities; Owner: -
--

ALTER TABLE ONLY symbol
    ADD CONSTRAINT symbol_exchange_id_fkey FOREIGN KEY (exchange_id) REFERENCES exchange(id);


-- Completed on 2016-03-24 14:31:58 BRT

--
-- PostgreSQL database dump complete
--

INSERT INTO data_vendor VALUES (1, 'Bovespa', 'http://bmf.bovespa.com.br', '', '2016-03-26 14:16:10.105345', '2016-03-26 14:16:10.105356');
INSERT INTO exchange VALUES (1, 'bov', 'bovespa', 'São Paulo', 'Brazil', 'R$', '00:00:00', '2016-03-26 14:16:10.135091', '2016-03-26 14:16:10.135099');
