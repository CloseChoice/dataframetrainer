import { defineConfig } from "cypress";
import pg from 'pg'
const {Pool} = pg
// Read the environment variables from the root file
import * as dotenv from 'dotenv'
dotenv.config({path: '../.env'})


import * as fs from 'fs'
const pgConnectionString = process.env.PG_CONNECTION_STRING
if (!pgConnectionString){
  throw new Error(`missing PG_CONNECTION_STRING environment variable`)
}


const pool = new Pool({
  connectionString : pgConnectionString
})
// Check if the database connection is succesfull
pool.query('SELECT NOW()')


const tasks = {
  'db:query': ({queryText, queryValues}) => {
    queryValues = queryValues ? queryValues : []
    return pool.query(queryText, queryValues)
  },
  'db:reseed': async () => {
    const sqlText = fs.readFileSync('./cypress/seed.sql', { encoding: 'utf8' })
    return pool.query(sqlText)
  }
}

export default defineConfig({
  // setupNodeEvents can be defined in either
  // the e2e or component configuration
  defaultCommandTimeout: 4000,
  env: {
    user: {
      // The User is inserted in the cypress/seed.sql script
      name: 'Bob',
      password: '1234'
    }
  },
  e2e: {
    baseUrl: 'http://localhost:5173',
    setupNodeEvents(on, config) {
      on('task', tasks)
    },
  },
})
