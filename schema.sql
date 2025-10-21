create extension if not exists pgcrypto;
create table if not exists users (
  id uuid primary key default gen_random_uuid(),
  email text unique not null,
  created_at timestamptz default now()
);
create table if not exists companies (
  id serial primary key,
  ticker text unique not null,
  name text,
  cik text
);
create table if not exists watchlists (
  user_id uuid references users(id) on delete cascade,
  company_id int references companies(id) on delete cascade,
  created_at timestamptz default now(),
  primary key (user_id, company_id)
);
create table if not exists filings (
  id bigserial primary key,
  company_id int references companies(id) on delete cascade,
  form text not null,
  filed_at date not null,
  title text,
  accession_no text,
  sec_url text
);
create table if not exists events (
  id bigserial primary key,
  company_id int references companies(id) on delete cascade,
  date date not null,
  type text not null,
  title text,
  source_url text,
  all_day boolean default true
);
create table if not exists reports (
  id bigserial primary key,
  user_id uuid references users(id) on delete cascade,
  period_start date,
  period_end date,
  summary_json jsonb,
  created_at timestamptz default now()
);
