--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5 (Homebrew)
-- Dumped by pg_dump version 17.5 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgis; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;


--
-- Name: EXTENSION postgis; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION postgis IS 'PostGIS geometry and geography spatial types and functions';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


--
-- Name: bus_lines; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.bus_lines (
    id integer NOT NULL,
    originar_ar character varying,
    originar_en character varying,
    color character varying,
    type character varying,
    busroute character varying,
    origin character varying,
    geometry public.geometry(MultiLineString,4326)
);


--
-- Name: bus_lines_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.bus_lines_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: bus_lines_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.bus_lines_id_seq OWNED BY public.bus_lines.id;


--
-- Name: neighborhoods; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.neighborhoods (
    neighborhood_id integer NOT NULL,
    neighborh_aname_ar character varying,
    neighborh_aname_en character varying,
    zoning_id integer,
    zoning_color character varying,
    price_of_meter character varying,
    shape_area character varying,
    transaction_price character varying,
    region_id integer,
    province_id integer,
    geometry public.geometry(Polygon,4326)
);


--
-- Name: neighborhoods_centroids; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.neighborhoods_centroids (
    id integer NOT NULL,
    neighborhood_id integer,
    neighborh_aname_ar character varying,
    neighborh_aname_en character varying,
    province_id integer,
    geometry public.geometry(Point,4326)
);


--
-- Name: neighborhoods_centroids_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.neighborhoods_centroids_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: neighborhoods_centroids_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.neighborhoods_centroids_id_seq OWNED BY public.neighborhoods_centroids.id;


--
-- Name: neighborhoods_neighborhood_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.neighborhoods_neighborhood_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: neighborhoods_neighborhood_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.neighborhoods_neighborhood_id_seq OWNED BY public.neighborhoods.neighborhood_id;


--
-- Name: parcel_buildingrules; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.parcel_buildingrules (
    id character varying NOT NULL,
    zoning_id integer,
    zoning_color character varying,
    zoning_group character varying,
    landuse character varying,
    description character varying,
    name character varying,
    coloring character varying,
    coloring_description character varying,
    max_building_coefficient character varying,
    max_building_height character varying,
    max_parcel_coverage character varying,
    max_rule_depth character varying,
    main_streets_setback character varying,
    secondary_streets_setback character varying,
    side_rear_setback character varying
);


--
-- Name: parcel_metrics_priceofmeter; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.parcel_metrics_priceofmeter (
    id integer NOT NULL,
    parcel_objid character varying,
    neighborhood_id integer,
    month integer,
    year integer,
    metrics_type character varying,
    average_price_of_meter character varying
);


--
-- Name: parcel_metrics_priceofmeter_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.parcel_metrics_priceofmeter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: parcel_metrics_priceofmeter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.parcel_metrics_priceofmeter_id_seq OWNED BY public.parcel_metrics_priceofmeter.id;


--
-- Name: parcels; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.parcels (
    parcel_objectid character varying NOT NULL,
    province_id integer,
    landuseagroup character varying,
    subdivision_no character varying,
    shape_area character varying,
    zoning_id integer,
    neighborhaname_ar character varying,
    neighborhaname_en character varying,
    neighborhood_id integer,
    municipality_aname_ar character varying,
    municipality_aname_en character varying,
    parcel_no character varying,
    subdivision_id character varying,
    transaction_price character varying,
    landuseadetailed character varying,
    parcel_id integer,
    price_of_meter character varying,
    zoning_color character varying,
    ruleid character varying,
    block_no character varying,
    geometry public.geometry(MultiPolygon,4326)
);


--
-- Name: parcels_base; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.parcels_base (
    parcel_objectid character varying NOT NULL,
    province_id integer,
    landuseagroup character varying,
    subdivision_no character varying,
    shape_area character varying,
    zoning_id integer,
    neighborhaname_ar character varying,
    neighborhaname_en character varying,
    neighborhood_id integer,
    municipality_aname_ar character varying,
    municipality_aname_en character varying,
    parcel_no character varying,
    subdivision_id character varying,
    transaction_price character varying,
    landuseadetailed character varying,
    parcel_id integer,
    price_of_meter character varying,
    zoning_color character varying,
    ruleid character varying,
    block_no character varying,
    geometry public.geometry(MultiPolygon,4326)
);


--
-- Name: parcels_centroids; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.parcels_centroids (
    id integer NOT NULL,
    parcel_id integer,
    parcel_no character varying,
    neighborhood_id integer,
    province_id integer,
    transactions_count integer,
    transaction_date character varying,
    transaction_price character varying,
    price_of_meter character varying,
    geometry public.geometry(Point,4326)
);


--
-- Name: parcels_centroids_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.parcels_centroids_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: parcels_centroids_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.parcels_centroids_id_seq OWNED BY public.parcels_centroids.id;


--
-- Name: parcels_final; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.parcels_final (
    id integer NOT NULL,
    geometry public.geometry(MultiPolygon,4326),
    h3_index character varying,
    attributes jsonb,
    enriched boolean,
    updated_at timestamp without time zone
);


--
-- Name: parcels_final_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.parcels_final_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: parcels_final_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.parcels_final_id_seq OWNED BY public.parcels_final.id;


--
-- Name: parcels_raw; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.parcels_raw (
    id integer NOT NULL,
    tile_id character varying,
    geometry public.geometry(MultiPolygon,4326),
    properties jsonb,
    ingested_at timestamp without time zone
);


--
-- Name: parcels_raw_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.parcels_raw_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: parcels_raw_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.parcels_raw_id_seq OWNED BY public.parcels_raw.id;


--
-- Name: provinces; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.provinces (
    province_id integer NOT NULL,
    province_name character varying,
    centroid_x double precision,
    centroid_y double precision
);


--
-- Name: provinces_province_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.provinces_province_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: provinces_province_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.provinces_province_id_seq OWNED BY public.provinces.province_id;


--
-- Name: qi_population_metrics; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.qi_population_metrics (
    grid_id character varying NOT NULL,
    population_density character varying,
    residential_rpi character varying,
    commercial_rpi character varying,
    poi_count character varying,
    geometry public.geometry(Polygon,4326)
);


--
-- Name: qi_stripes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.qi_stripes (
    strip_id character varying NOT NULL,
    centroid_longitude character varying,
    centroid_latitude character varying,
    geometry public.geometry(Polygon,4326)
);


--
-- Name: regions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.regions (
    region_id integer NOT NULL,
    region_name character varying,
    province_id integer,
    centroid_x double precision,
    centroid_y double precision,
    bounding_box_sw_x double precision,
    bounding_box_sw_y double precision,
    bounding_box_ne_x double precision,
    bounding_box_ne_y double precision,
    slug character varying
);


--
-- Name: regions_region_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.regions_region_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: regions_region_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.regions_region_id_seq OWNED BY public.regions.region_id;


--
-- Name: riyadh_bus_stations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.riyadh_bus_stations (
    station_code character varying NOT NULL,
    station_name_ar character varying,
    station_name_en character varying,
    station_long character varying,
    station_lat character varying,
    geometry public.geometry(Point,4326)
);


--
-- Name: subdivisions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.subdivisions (
    subdivision_id integer NOT NULL,
    subdivision_no character varying,
    zoning_id integer,
    zoning_color character varying,
    transaction_price character varying,
    price_of_meter character varying,
    shape_area character varying,
    province_id integer,
    geometry public.geometry(MultiPolygon,4326)
);


--
-- Name: subdivisions_subdivision_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.subdivisions_subdivision_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: subdivisions_subdivision_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.subdivisions_subdivision_id_seq OWNED BY public.subdivisions.subdivision_id;


--
-- Name: tile_state; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tile_state (
    id integer NOT NULL,
    tile_id character varying,
    status character varying,
    last_updated timestamp without time zone,
    error character varying
);


--
-- Name: tile_state_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tile_state_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tile_state_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.tile_state_id_seq OWNED BY public.tile_state.id;


--
-- Name: transactions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.transactions (
    transaction_number integer NOT NULL,
    transaction_date character varying,
    transaction_price character varying,
    price_of_meter character varying,
    parcel_objectid character varying,
    parcel_id integer,
    parcel_no character varying,
    block_no character varying,
    area character varying,
    zoning_id integer,
    neighborhood_id integer,
    region_id integer,
    province_id integer,
    subdivision_no character varying,
    subdivision_id character varying,
    centroid_x character varying,
    centroid_y character varying,
    metrics_type character varying,
    landuseagroup character varying,
    landuseadetailed character varying,
    geometry public.geometry(MultiPolygon,4326)
);


--
-- Name: transactions_transaction_number_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.transactions_transaction_number_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: transactions_transaction_number_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.transactions_transaction_number_seq OWNED BY public.transactions.transaction_number;


--
-- Name: bus_lines id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bus_lines ALTER COLUMN id SET DEFAULT nextval('public.bus_lines_id_seq'::regclass);


--
-- Name: neighborhoods neighborhood_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.neighborhoods ALTER COLUMN neighborhood_id SET DEFAULT nextval('public.neighborhoods_neighborhood_id_seq'::regclass);


--
-- Name: neighborhoods_centroids id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.neighborhoods_centroids ALTER COLUMN id SET DEFAULT nextval('public.neighborhoods_centroids_id_seq'::regclass);


--
-- Name: parcel_metrics_priceofmeter id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parcel_metrics_priceofmeter ALTER COLUMN id SET DEFAULT nextval('public.parcel_metrics_priceofmeter_id_seq'::regclass);


--
-- Name: parcels_centroids id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parcels_centroids ALTER COLUMN id SET DEFAULT nextval('public.parcels_centroids_id_seq'::regclass);


--
-- Name: parcels_final id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parcels_final ALTER COLUMN id SET DEFAULT nextval('public.parcels_final_id_seq'::regclass);


--
-- Name: parcels_raw id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parcels_raw ALTER COLUMN id SET DEFAULT nextval('public.parcels_raw_id_seq'::regclass);


--
-- Name: provinces province_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.provinces ALTER COLUMN province_id SET DEFAULT nextval('public.provinces_province_id_seq'::regclass);


--
-- Name: regions region_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.regions ALTER COLUMN region_id SET DEFAULT nextval('public.regions_region_id_seq'::regclass);


--
-- Name: subdivisions subdivision_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.subdivisions ALTER COLUMN subdivision_id SET DEFAULT nextval('public.subdivisions_subdivision_id_seq'::regclass);


--
-- Name: tile_state id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tile_state ALTER COLUMN id SET DEFAULT nextval('public.tile_state_id_seq'::regclass);


--
-- Name: transactions transaction_number; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.transactions ALTER COLUMN transaction_number SET DEFAULT nextval('public.transactions_transaction_number_seq'::regclass);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: bus_lines bus_lines_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.bus_lines
    ADD CONSTRAINT bus_lines_pkey PRIMARY KEY (id);


--
-- Name: neighborhoods_centroids neighborhoods_centroids_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.neighborhoods_centroids
    ADD CONSTRAINT neighborhoods_centroids_pkey PRIMARY KEY (id);


--
-- Name: neighborhoods neighborhoods_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.neighborhoods
    ADD CONSTRAINT neighborhoods_pkey PRIMARY KEY (neighborhood_id);


--
-- Name: parcel_buildingrules parcel_buildingrules_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parcel_buildingrules
    ADD CONSTRAINT parcel_buildingrules_pkey PRIMARY KEY (id);


--
-- Name: parcel_metrics_priceofmeter parcel_metrics_priceofmeter_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parcel_metrics_priceofmeter
    ADD CONSTRAINT parcel_metrics_priceofmeter_pkey PRIMARY KEY (id);


--
-- Name: parcels_base parcels_base_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parcels_base
    ADD CONSTRAINT parcels_base_pkey PRIMARY KEY (parcel_objectid);


--
-- Name: parcels_centroids parcels_centroids_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parcels_centroids
    ADD CONSTRAINT parcels_centroids_pkey PRIMARY KEY (id);


--
-- Name: parcels_final parcels_final_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parcels_final
    ADD CONSTRAINT parcels_final_pkey PRIMARY KEY (id);


--
-- Name: parcels parcels_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parcels
    ADD CONSTRAINT parcels_pkey PRIMARY KEY (parcel_objectid);


--
-- Name: parcels_raw parcels_raw_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.parcels_raw
    ADD CONSTRAINT parcels_raw_pkey PRIMARY KEY (id);


--
-- Name: provinces provinces_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.provinces
    ADD CONSTRAINT provinces_pkey PRIMARY KEY (province_id);


--
-- Name: qi_population_metrics qi_population_metrics_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.qi_population_metrics
    ADD CONSTRAINT qi_population_metrics_pkey PRIMARY KEY (grid_id);


--
-- Name: qi_stripes qi_stripes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.qi_stripes
    ADD CONSTRAINT qi_stripes_pkey PRIMARY KEY (strip_id);


--
-- Name: regions regions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.regions
    ADD CONSTRAINT regions_pkey PRIMARY KEY (region_id);


--
-- Name: riyadh_bus_stations riyadh_bus_stations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.riyadh_bus_stations
    ADD CONSTRAINT riyadh_bus_stations_pkey PRIMARY KEY (station_code);


--
-- Name: subdivisions subdivisions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.subdivisions
    ADD CONSTRAINT subdivisions_pkey PRIMARY KEY (subdivision_id);


--
-- Name: tile_state tile_state_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tile_state
    ADD CONSTRAINT tile_state_pkey PRIMARY KEY (id);


--
-- Name: tile_state tile_state_tile_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tile_state
    ADD CONSTRAINT tile_state_tile_id_key UNIQUE (tile_id);


--
-- Name: transactions transactions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (transaction_number);


--
-- Name: app_parcels_final_geometry_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX app_parcels_final_geometry_idx ON public.parcels_final USING gist (geometry);


--
-- Name: app_parcels_raw_geometry_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX app_parcels_raw_geometry_idx ON public.parcels_raw USING gist (geometry);


--
-- PostgreSQL database dump complete
--

