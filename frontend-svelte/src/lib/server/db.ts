/* eslint-disable @typescript-eslint/no-explicit-any */
import { type QueryResult, Pool} from 'pg'

import { 
  PG_CONNECTION_STRING,
} from "$env/static/private";

if (!PG_CONNECTION_STRING){
  throw new Error(`missing PG_CONNECTION_STRING environment variable`)
}

export const pool = new Pool({
  connectionString : PG_CONNECTION_STRING
})

