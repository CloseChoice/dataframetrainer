/* eslint-disable @typescript-eslint/no-explicit-any */
import type { QueryResult} from 'pg'
import pg from 'pg'
import { env } from '$env/dynamic/private';
// import { DATABASE_URL } from '$env/static/private'

// This makes the keys in dotenv available 
import 'dotenv/config'

const PGUSER="postgres"
const PGPASSWORD="example"
const PGPORT="5432"
const PGHOST="127.0.0.1"
const PGDATABASE="postgres"

const pool = new pg.Pool({
  max: 10, // default
  password:PGPASSWORD,
  host: PGHOST,
  database: PGDATABASE,
  port: PGPORT,
  user: PGUSER,
//   ssl: { // If your postgresql.conf does not have `ssl = on`, remove the entire ssl property or you will get an error
//     rejectUnauthorized: false
//   }
})

type PostgresQueryResult = (sql: string, params?: any[]) => Promise<QueryResult<any>>
export const query: PostgresQueryResult = (sql, params?) => pool.query(sql, params)