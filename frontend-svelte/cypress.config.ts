import { defineConfig } from "cypress";
import * as fs from 'fs';
import pg from 'pg'
import * as dotenv from 'dotenv'
dotenv.config({path: '../.env'})

const {DB_NAME, DB_USER, PASSWORD, PORT} = process.env
const PG_CONNECTION_STRING = `postgres://${DB_USER}:${PASSWORD}@localhost:${PORT}/${DB_NAME}`
const pool = new pg.Pool({connectionString : PG_CONNECTION_STRING})



const tasks = {
  // Since all Values in the tests are hard coded anyways the queryText has to be "baked" when using db:query 
  'db:query': (queryText) => {
    return pool.query(queryText)
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
    retries: {
      "runMode": 2,
      "openMode": 2
    }
  },
})
