/* eslint-disable @typescript-eslint/no-explicit-any */
import { type QueryResult, Pool} from 'pg'

import { 
  PGUSER, PGPASSWORD, PGPORT, PGHOST,
  } from "$env/static/private";

const PG_CONNECTION_STRING = `postgres://${PGUSER}:${PGPASSWORD}@${PGHOST}:${PGPORT}/postgres`

if (!PG_CONNECTION_STRING){
  throw new Error(`missing PG_CONNECTION_STRING environment variable`)
}

export const pool = new Pool({
  connectionString : PG_CONNECTION_STRING
})

