/* eslint-disable @typescript-eslint/no-explicit-any */
import { type QueryResult, Pool} from 'pg'

import {DB_NAME, DB_USER, HOST, PASSWORD, PORT} from '$env/static/private'
const PG_CONNECTION_STRING = `postgres://${DB_USER}:${PASSWORD}@${HOST}:${PORT}/${DB_NAME}`

console.log(PG_CONNECTION_STRING);

if (!PG_CONNECTION_STRING){
  throw new Error(`missing PG_CONNECTION_STRING environment variable`)
}

export const pool = new Pool({
  connectionString : PG_CONNECTION_STRING
})

