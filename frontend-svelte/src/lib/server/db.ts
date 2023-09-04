/* eslint-disable @typescript-eslint/no-explicit-any */
import pg from 'pg'
import {DB_NAME, DB_USER, PASSWORD, PORT} from '$env/static/private'

if (!(DB_NAME && DB_USER && PASSWORD && PORT)){
  throw new Error("Not all environment variables are defined")
}
export const PG_CONNECTION_STRING = `postgres://${DB_USER}:${PASSWORD}@db:${PORT}/${DB_NAME}`

if (!PG_CONNECTION_STRING){
  throw new Error(`missing PG_CONNECTION_STRING environment variable`)
}

export const pool = new pg.Pool({
  connectionString : PG_CONNECTION_STRING
})
