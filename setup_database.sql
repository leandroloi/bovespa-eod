SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 8 (class 2615 OID 22853)
-- Name: historic; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA historic;

SET search_path = historic, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 174 (class 1259 OID 22874)
-- Name: codbdi; Type: TABLE; Schema: historic; Owner: -; Tablespace:
--

CREATE TABLE "codbdi" (
    id integer,
    description character varying
);


--
-- TOC entry 177 (class 1259 OID 22910)
-- Name: spot; Type: TABLE; Schema: historic; Owner: -; Tablespace:
--

CREATE TABLE "spot" (
    price_date timestamp without time zone,
    cod_dbi bigint,
    ticker character(12),
    tpmerc bigint,
    especi character varying(10),
    prazot character varying(3),
    open_price numeric(19,4),
    high_price numeric(19,4),
    low_price numeric(19,4),
    avg_price numeric(19,4),
    close_price numeric(19,4),
    preofc numeric(19,4),
    preofv numeric(19,4),
    totneg bigint,
    quatot bigint,
    volume bigint,
    preexe numeric(19,4),
    indopc bigint,
    datven timestamp without time zone,
    fatcot bigint,
    ptoexec numeric(19,4),
    codisi character varying(12),
    dismes bigint,
    primary key (price_date, ticker)
);

CREATE TABLE "option" (
    price_date timestamp without time zone,
    cod_dbi bigint,
    ticker character(12),
    tpmerc bigint,
    especi character varying(10),
    prazot character varying(3),
    open_price numeric(19,4),
    high_price numeric(19,4),
    low_price numeric(19,4),
    avg_price numeric(19,4),
    close_price numeric(19,4),
    preofc numeric(19,4),
    preofv numeric(19,4),
    totneg bigint,
    quatot bigint,
    volume bigint,
    preexe numeric(19,4),
    indopc bigint,
    datven date,
    fatcot bigint,
    ptoexec numeric(19,4),
    codisi character varying(12),
    dismes bigint,
    primary key (price_date, ticker)
);

CREATE TABLE "auction" (
    price_date timestamp without time zone,
    cod_dbi bigint,
    ticker character(12),
    tpmerc bigint,
    especi character varying(10),
    prazot character varying(3),
    open_price numeric(19,4),
    high_price numeric(19,4),
    low_price numeric(19,4),
    avg_price numeric(19,4),
    close_price numeric(19,4),
    preofc numeric(19,4),
    preofv numeric(19,4),
    totneg bigint,
    quatot bigint,
    volume bigint,
    preexe numeric(19,4),
    indopc bigint,
    datven timestamp without time zone,
    fatcot bigint,
    ptoexec numeric(19,4),
    codisi character varying(12),
    dismes bigint,
    primary key (price_date, ticker)
);

CREATE TABLE "fractionary" (
    price_date timestamp without time zone,
    cod_dbi bigint,
    ticker character(12),
    tpmerc bigint,
    especi character varying(10),
    prazot character varying(3),
    open_price numeric(19,4),
    high_price numeric(19,4),
    low_price numeric(19,4),
    avg_price numeric(19,4),
    close_price numeric(19,4),
    preofc numeric(19,4),
    preofv numeric(19,4),
    totneg bigint,
    quatot bigint,
    volume bigint,
    preexe numeric(19,4),
    indopc bigint,
    datven timestamp without time zone,
    fatcot bigint,
    ptoexec numeric(19,4),
    codisi character varying(12),
    dismes bigint,
    primary key (price_date, ticker)
);

CREATE TABLE "term" (
    price_date timestamp without time zone,
    cod_dbi bigint,
    ticker character(12),
    tpmerc bigint,
    especi character varying(10),
    prazot character varying(3),
    open_price numeric(19,4),
    high_price numeric(19,4),
    low_price numeric(19,4),
    avg_price numeric(19,4),
    close_price numeric(19,4),
    preofc numeric(19,4),
    preofv numeric(19,4),
    totneg bigint,
    quatot bigint,
    volume bigint,
    preexe numeric(19,4),
    indopc bigint,
    datven timestamp without time zone,
    fatcot bigint,
    ptoexec numeric(19,4),
    codisi character varying(12),
    dismes bigint,
    primary key (price_date, ticker, prazot)
);

CREATE TABLE "future" (
    price_date timestamp without time zone,
    cod_dbi bigint,
    ticker character(12),
    tpmerc bigint,
    especi character varying(10),
    prazot character varying(3),
    open_price numeric(19,4),
    high_price numeric(19,4),
    low_price numeric(19,4),
    avg_price numeric(19,4),
    close_price numeric(19,4),
    preofc numeric(19,4),
    preofv numeric(19,4),
    totneg bigint,
    quatot bigint,
    volume bigint,
    preexe numeric(19,4),
    indopc bigint,
    datven timestamp without time zone,
    fatcot bigint,
    ptoexec numeric(19,4),
    codisi character varying(12),
    dismes bigint,
    primary key (price_date, ticker)
);


--
-- TOC entry 175 (class 1259 OID 22889)
-- Name: especi; Type: TABLE; Schema: historic; Owner: -; Tablespace:
--

CREATE TABLE "especi" (
    type character varying,
    description character varying
);


--
-- TOC entry 173 (class 1259 OID 22868)
-- Name: identi; Type: TABLE; Schema: historic; Owner: -; Tablespace:
--

CREATE TABLE "identi" (
    id integer,
    indexes character varying(32),
    description character varying
);


--
-- TOC entry 172 (class 1259 OID 22854)
-- Name: indopc; Type: TABLE; Schema: historic; Owner: -; Tablespace:
--

CREATE TABLE "indopc" (
    id integer NOT NULL,
    indicator character varying(32),
    description character varying
);


--
-- TOC entry 176 (class 1259 OID 22901)
-- Name: tpmerc; Type: TABLE; Schema: historic; Owner: -; Tablespace:
--

CREATE TABLE "tpmerc" (
    id integer,
    description character varying
);


--
-- TOC entry 2910 (class 0 OID 22874)
-- Dependencies: 174
-- Data for Name: codbdi; Type: TABLE DATA; Schema: historic; Owner: -
--

INSERT INTO "codbdi" (id, description) VALUES (2, 'LOTE PADRÃO');
INSERT INTO "codbdi" (id, description) VALUES (6, 'CONCORDATÁRIAS');
INSERT INTO "codbdi" (id, description) VALUES (10, 'DIREITOS E RECIBOS');
INSERT INTO "codbdi" (id, description) VALUES (12, 'FUNDOS IMOBILIÁRIOS');
INSERT INTO "codbdi" (id, description) VALUES (14, 'CERTIFIC. INVESTIMENTO / DEBÊNTURES / TÍTULOS DIVIDA PÚBLICA');
INSERT INTO "codbdi" (id, description) VALUES (18, 'OBRIGAÇÕES');
INSERT INTO "codbdi" (id, description) VALUES (22, 'BÔNUS (PRIVADOS)');
INSERT INTO "codbdi" (id, description) VALUES (26, 'APÓLICES / BÔNUS / TÍTULOS PÚBLICOS');
INSERT INTO "codbdi" (id, description) VALUES (32, 'EXERCÍCIO DE OPÇÕES DE COMPRA DE ÍNDICE');
INSERT INTO "codbdi" (id, description) VALUES (33, 'EXERCÍCIO DE OPÇÕES DE VENDA DE ÍNDICE');
INSERT INTO "codbdi" (id, description) VALUES (38, 'EXERCÍCIO DE OPÇÕES DE COMPRA');
INSERT INTO "codbdi" (id, description) VALUES (42, 'EXERCÍCIO DE OPÇÕES DE VENDA');
INSERT INTO "codbdi" (id, description) VALUES (46, 'LEILÃO DE TÍTULOS NÃO COTADOS');
INSERT INTO "codbdi" (id, description) VALUES (48, 'LEILÃO DE PRIVATIZAÇÃO');
INSERT INTO "codbdi" (id, description) VALUES (50, 'LEILÃO');
INSERT INTO "codbdi" (id, description) VALUES (51, 'LEILÃO FINOR');
INSERT INTO "codbdi" (id, description) VALUES (52, 'LEILÃO FINAM');
INSERT INTO "codbdi" (id, description) VALUES (53, 'LEILÃO FISET');
INSERT INTO "codbdi" (id, description) VALUES (54, 'LEILÃO DE AÇÕES EM MORA');
INSERT INTO "codbdi" (id, description) VALUES (56, 'VENDAS POR ALVARÁ JUDICIAL');
INSERT INTO "codbdi" (id, description) VALUES (58, 'OUTROS');
INSERT INTO "codbdi" (id, description) VALUES (60, 'PERMUTA POR AÇÕES');
INSERT INTO "codbdi" (id, description) VALUES (61, 'META');
INSERT INTO "codbdi" (id, description) VALUES (62, 'TERMO');
INSERT INTO "codbdi" (id, description) VALUES (66, 'DEBÊNTURES COM DATA DE VENCIMENTO ATÉ 3 ANOS');
INSERT INTO "codbdi" (id, description) VALUES (68, 'DEBÊNTURES COM DATA DE VENCIMENTO MAIOR QUE 3 ANOS');
INSERT INTO "codbdi" (id, description) VALUES (70, 'FUTURO COM MOVIMENTAÇÃO CONTÍNUA');
INSERT INTO "codbdi" (id, description) VALUES (71, 'FUTURO COM RETENÇÃO DE GANHO');
INSERT INTO "codbdi" (id, description) VALUES (74, 'OPÇÕES DE COMPRA DE ÍNDICES');
INSERT INTO "codbdi" (id, description) VALUES (75, 'OPÇÕES DE VENDA DE ÍNDICES');
INSERT INTO "codbdi" (id, description) VALUES (78, 'OPÇÕES DE COMPRA');
INSERT INTO "codbdi" (id, description) VALUES (82, 'OPÇÕES DE VENDA');
INSERT INTO "codbdi" (id, description) VALUES (83, 'DEBÊNTURES E NOTAS PROMISSÓRIAS');
INSERT INTO "codbdi" (id, description) VALUES (96, 'FRACIONÁRIO');
INSERT INTO "codbdi" (id, description) VALUES (99, 'TOTAL GERAL');


--
-- TOC entry 2913 (class 0 OID 22910)
-- Dependencies: 177
-- Data for Name: spot; Type: TABLE DATA; Schema: historic; Owner: -
--



--
-- TOC entry 2911 (class 0 OID 22889)
-- Dependencies: 175
-- Data for Name: especi; Type: TABLE DATA; Schema: historic; Owner: -
--

INSERT INTO "especi" (type, description) VALUES ('ON', 'AÇÕES ORDINÁRIAS NOMINATIVAS');
INSERT INTO "especi" (type, description) VALUES ('PNA', ' AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE A');
INSERT INTO "especi" (type, description) VALUES ('PNB', ' AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE B');
INSERT INTO "especi" (type, description) VALUES ('PNC', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE C');
INSERT INTO "especi" (type, description) VALUES ('PND', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE D');
INSERT INTO "especi" (type, description) VALUES ('PNE', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE');
INSERT INTO "especi" (type, description) VALUES ('PNF', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE F');
INSERT INTO "especi" (type, description) VALUES ('PNG', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE G');
INSERT INTO "especi" (type, description) VALUES ('PNH', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE H');
INSERT INTO "especi" (type, description) VALUES ('PN', 'AÇÕES PREFERENCIAIS NOMINATIVAS');
INSERT INTO "especi" (type, description) VALUES ('PNV', 'AÇÕES PREFERENCIAIS NOMINATIVAS COM DIREITO A VOTO');
INSERT INTO "especi" (type, description) VALUES ('OR', 'AÇÕES ORDINÁRIAS NOMINATIVAS RESGATÁVEIS');
INSERT INTO "especi" (type, description) VALUES ('PRA', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE A RESGATÁVEIS');
INSERT INTO "especi" (type, description) VALUES ('PRB', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE B RESGATÁVEIS');
INSERT INTO "especi" (type, description) VALUES ('PRC', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE C RESGATÁVEIS');
INSERT INTO "especi" (type, description) VALUES ('PRD', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE D RESGATÁVEIS');
INSERT INTO "especi" (type, description) VALUES ('PRE', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE E RESGATÁVEIS');
INSERT INTO "especi" (type, description) VALUES ('PRF', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE F RESGATÁVEIS');
INSERT INTO "especi" (type, description) VALUES ('PRG', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE G RESGATÁVEIS');
INSERT INTO "especi" (type, description) VALUES ('PRH', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE H RESGATÁVEIS');
INSERT INTO "especi" (type, description) VALUES ('PNR', 'AÇÕES PREFERENCIAIS NOMINATIVAS RESGATÁVEIS');
INSERT INTO "especi" (type, description) VALUES ('PRV', 'AÇÕES PREFERENCIAIS NOMINATIVAS COM DIREITO A VOTO RESG');
INSERT INTO "especi" (type, description) VALUES ('ON P', 'AÇÕES ORDINÁRIAS NOMINATIVAS COM DIREITOS DIFERENCIADOS');
INSERT INTO "especi" (type, description) VALUES ('PNA P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE A C/ DIREITOS DIFER');
INSERT INTO "especi" (type, description) VALUES ('PNB P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE B C/ DIREITOS DIFER');
INSERT INTO "especi" (type, description) VALUES ('PNC P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE C C/ DIREITOS DIFER');
INSERT INTO "especi" (type, description) VALUES ('PND P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE D C/ DIREITOS DIFER');
INSERT INTO "especi" (type, description) VALUES ('PNE P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE E C/ DIREITOS DIFER');
INSERT INTO "especi" (type, description) VALUES ('PNF P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE F C/ DIREITOS DIFER');
INSERT INTO "especi" (type, description) VALUES ('PNG P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE G C/ DIREITOS DIFER');
INSERT INTO "especi" (type, description) VALUES ('PNH P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE H C/ DIREITOS DIFER');
INSERT INTO "especi" (type, description) VALUES ('PN P', 'AÇÕES PREFERENCIAIS NOMINATIVAS COM DIREITOS DIFERENCIADOS');
INSERT INTO "especi" (type, description) VALUES ('PNV P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE V C/ DIREITOS DIFER');
INSERT INTO "especi" (type, description) VALUES ('ON P', 'AÇÕES ORDINÁRIAS NOMINATIVAS COM DIREITOS DIFERENCIADOS');
INSERT INTO "especi" (type, description) VALUES ('BDR', 'BDR');
INSERT INTO "especi" (type, description) VALUES ('UNT', 'CERTIFICADO DE DEPOSITO DE AÇÕES - MISCELÂNEA');
INSERT INTO "especi" (type, description) VALUES ('CDA', 'CERTIFICADO DE DEPOSITO DE AÇÕES ORDINÁRIAS');
INSERT INTO "especi" (type, description) VALUES ('CPA', 'CERTIFICADOS DE POTENCIAL ADICIONAL DE CONSTRUÇÃO E OPERAÇÃO');
INSERT INTO "especi" (type, description) VALUES ('RON', 'CESTA DE AÇÕES ORDINÁRIAS NOMINATIVAS');
INSERT INTO "especi" (type, description) VALUES ('R', 'CESTA DE AÇÕES NOMINATIVAS');
INSERT INTO "especi" (type, description) VALUES ('CI', 'FUNDO DE INVESTIMENTO');
INSERT INTO "especi" (type, description) VALUES ('DIR', 'DIREITOS DE SUBSCRIÇÃO MISCELÂNEA (BÔNUS, DEBÊNTURES, ETC)');
INSERT INTO "especi" (type, description) VALUES ('DIR ORD', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES ORDINÁRIAS');
INSERT INTO "especi" (type, description) VALUES ('DIR P/A', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE A');
INSERT INTO "especi" (type, description) VALUES ('DIR P/B', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE B');
INSERT INTO "especi" (type, description) VALUES ('DIR P/C', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE C');
INSERT INTO "especi" (type, description) VALUES ('DIR P/D', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE D');
INSERT INTO "especi" (type, description) VALUES ('DIR P/E', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE E');
INSERT INTO "especi" (type, description) VALUES ('DIR P/F', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE F');
INSERT INTO "especi" (type, description) VALUES ('DIR P/G', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE G');
INSERT INTO "especi" (type, description) VALUES ('DIR P/H', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE H');
INSERT INTO "especi" (type, description) VALUES ('DIR PRE', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS');
INSERT INTO "especi" (type, description) VALUES ('PRA REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE A');
INSERT INTO "especi" (type, description) VALUES ('PRB REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE B');
INSERT INTO "especi" (type, description) VALUES ('PRC REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE C');
INSERT INTO "especi" (type, description) VALUES ('M1 REC', 'RECIBO DE SUBSCRIÇÃO DE MISCELÂNEAS');
INSERT INTO "especi" (type, description) VALUES ('DIR PRA', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE A');
INSERT INTO "especi" (type, description) VALUES ('DIR PRB', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE B');
INSERT INTO "especi" (type, description) VALUES ('DIR PRC', 'DIREITOS DE SUBSCRIÇÃO EM AÇÕES RESGATÁVEIS PREF. CLASSE C');
INSERT INTO "especi" (type, description) VALUES ('LFT', 'LETRA FINANCEIRA DO TESOURO');
INSERT INTO "especi" (type, description) VALUES ('BNS ORD', 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES ORDINÁRIAS');
INSERT INTO "especi" (type, description) VALUES ('BNS P/A', 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE A');
INSERT INTO "especi" (type, description) VALUES ('BNS P/B', 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE B');
INSERT INTO "especi" (type, description) VALUES ('BNS P/C', 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE C');
INSERT INTO "especi" (type, description) VALUES ('BNS P/D', 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE D');
INSERT INTO "especi" (type, description) VALUES ('BNS P/E', 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE E');
INSERT INTO "especi" (type, description) VALUES ('BNS P/F', 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE F');
INSERT INTO "especi" (type, description) VALUES ('BNS P/G', 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE G');
INSERT INTO "especi" (type, description) VALUES ('BNS P/H', 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE H');
INSERT INTO "especi" (type, description) VALUES ('BNS PRE', 'BÔNUS DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS');
INSERT INTO "especi" (type, description) VALUES ('PCD', 'POSIÇÃO CONSOLIDADA DA DIVIDA');
INSERT INTO "especi" (type, description) VALUES ('UP', 'PRECATÓRIO');
INSERT INTO "especi" (type, description) VALUES ('REC', 'RECIBO DE SUBSCRIÇÃO MISCELÂNEA');
INSERT INTO "especi" (type, description) VALUES ('ON REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES ORDINÁRIAS');
INSERT INTO "especi" (type, description) VALUES ('PNA REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE A');
INSERT INTO "especi" (type, description) VALUES ('PNB REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE B');
INSERT INTO "especi" (type, description) VALUES ('PNC REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE C');
INSERT INTO "especi" (type, description) VALUES ('PND REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE D');
INSERT INTO "especi" (type, description) VALUES ('PNE REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE E');
INSERT INTO "especi" (type, description) VALUES ('PNF REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE F');
INSERT INTO "especi" (type, description) VALUES ('PNG REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE G');
INSERT INTO "especi" (type, description) VALUES ('PNH REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS CLASSE H');
INSERT INTO "especi" (type, description) VALUES ('PN REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS');
INSERT INTO "especi" (type, description) VALUES ('PNV REC', 'RECIBO DE SUBSCRIÇÃO EM AÇÕES PREFERENCIAIS C/ DIREITO VOTO');
INSERT INTO "especi" (type, description) VALUES ('UNT', 'UNITS');
INSERT INTO "especi" (type, description) VALUES ('WRT', 'WARRANTS DE DEBÊNTURES');
INSERT INTO "especi" (type, description) VALUES ('OR P', 'AÇÕES ORDINÁRIAS NOMINATIVAS RESGATÁVEIS C/ DIREITOS DIF');
INSERT INTO "especi" (type, description) VALUES ('PRA P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE "A" RESG. C/ DIR.DIF');
INSERT INTO "especi" (type, description) VALUES ('PRB P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE "B" RESG. C/ DIR.DIF');
INSERT INTO "especi" (type, description) VALUES ('PRC P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE "C" RESG. C/ DIR.DIF');
INSERT INTO "especi" (type, description) VALUES ('PRD P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE "D" RESG. C/ DIR.DIF.');
INSERT INTO "especi" (type, description) VALUES ('PRE P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE "E" RESG. C/ DIR.DIF');
INSERT INTO "especi" (type, description) VALUES ('PRF P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE "F" RESG. C/ DIR.DIF.');
INSERT INTO "especi" (type, description) VALUES ('PRG P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE "G" RESG. C/ DIR.DIF');
INSERT INTO "especi" (type, description) VALUES ('PRH P', 'AÇÕES PREFERENCIAIS NOMINATIVAS CLASSE "H" RESG. C/ DIR.DIF');
INSERT INTO "especi" (type, description) VALUES ('PR P', 'AÇÕES PREFERENCIAIS NOMINATIVAS RESGATÁVEIS C/ DIREITOS DIF');
INSERT INTO "especi" (type, description) VALUES ('PRV P', 'AÇÕES PREFERENCIAIS NOMINATIVAS RESG. C/ DIR.DIF. E DIR.VOTO');


--
-- TOC entry 2909 (class 0 OID 22868)
-- Dependencies: 173
-- Data for Name: identi; Type: TABLE DATA; Schema: historic; Owner: -
--

INSERT INTO "identi" (id, indexes, description) VALUES (1, 'IBOV', 'ÍNDICE BOVESPA');
INSERT INTO "identi" (id, indexes, description) VALUES (2, 'IEEX', 'ÍNDICE SETORIAL DE ENERGIA ELÉTRICA');
INSERT INTO "identi" (id, indexes, description) VALUES (3, 'IVBX', 'ÍNDICE IVBX2');
INSERT INTO "identi" (id, indexes, description) VALUES (4, 'IBXX', 'ÍNDICE IBRX BRASIL');
INSERT INTO "identi" (id, indexes, description) VALUES (5, 'ITEL', 'ÍNDICE ITELECOM');
INSERT INTO "identi" (id, indexes, description) VALUES (6, 'IBXL', 'ÍNDICE IBRX 50');
INSERT INTO "identi" (id, indexes, description) VALUES (7, 'MIBV', 'MINI IBOV');
INSERT INTO "identi" (id, indexes, description) VALUES (8, 'IGCX', 'ÍNDICE IGOVERNANÇA');
INSERT INTO "identi" (id, indexes, description) VALUES (10, 'ITAG', 'ITAG ALONG');


--
-- TOC entry 2908 (class 0 OID 22854)
-- Dependencies: 172
-- Data for Name: indopc; Type: TABLE DATA; Schema: historic; Owner: -
--

INSERT INTO "indopc" (id, indicator, description) VALUES (1, 'US$', 'CORREÇÃO PELA TAXA DO DÓLAR');
INSERT INTO "indopc" (id, indicator, description) VALUES (2, 'TJLP', 'CORREÇÃO PELA TJLP');
INSERT INTO "indopc" (id, indicator, description) VALUES (3, 'TR', 'CORREÇÃO PELA TR');
INSERT INTO "indopc" (id, indicator, description) VALUES (4, 'IPCR', 'CORREÇÃO PELO IPCR');
INSERT INTO "indopc" (id, indicator, description) VALUES (5, 'SWA', 'OPÇÕES DE TROCA - SWOPTIONS');
INSERT INTO "indopc" (id, indicator, description) VALUES (6, 'ÍNDICES', 'OPÇÕES REFERENCIADAS EM PONTOS DE ÍNDICE');
INSERT INTO "indopc" (id, indicator, description) VALUES (7, 'US$', 'CORREÇÃO PELA TAXA DO DÓLAR - OPÇÕES PROTEGIDAS');
INSERT INTO "indopc" (id, indicator, description) VALUES (8, 'IGPM', 'CORREÇÃO PELO IGP-M - OPÇÕES PROTEGIDAS');
INSERT INTO "indopc" (id, indicator, description) VALUES (9, 'URV', 'CORREÇÃO PELA URV');


--
-- TOC entry 2912 (class 0 OID 22901)
-- Dependencies: 176
-- Data for Name: tpmerc; Type: TABLE DATA; Schema: historic; Owner: -
--

INSERT INTO "tpmerc" (id, description) VALUES (10, 'VISTA');
INSERT INTO "tpmerc" (id, description) VALUES (12, 'EXERCÍCIO DE OPÇÕES DE COMPRA');
INSERT INTO "tpmerc" (id, description) VALUES (13, 'EXERCÍCIO DE OPÇÕES DE VENDA');
INSERT INTO "tpmerc" (id, description) VALUES (17, 'LEILÃO');
INSERT INTO "tpmerc" (id, description) VALUES (20, 'FRACIONÁRIO');
INSERT INTO "tpmerc" (id, description) VALUES (30, 'TERMO');
INSERT INTO "tpmerc" (id, description) VALUES (50, 'FUTURO COM RETENÇÃO DE GANHO');
INSERT INTO "tpmerc" (id, description) VALUES (60, 'FUTURO COM MOVIMENTAÇÃO CONTÍNUA');
INSERT INTO "tpmerc" (id, description) VALUES (70, 'OPÇÕES DE COMPRA');
INSERT INTO "tpmerc" (id, description) VALUES (80, 'OPÇÕES DE VENDA');


--
-- TOC entry 2800 (class 2606 OID 22861)
-- Name: id; Type: CONSTRAINT; Schema: historic; Owner: -; Tablespace:
--

ALTER TABLE ONLY "indopc"
    ADD CONSTRAINT id PRIMARY KEY (id);


-- Completed on 2016-03-31 12:45:32 BRT

--
-- PostgreSQL database dump complete
--