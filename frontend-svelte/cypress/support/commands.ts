/// <reference types="cypress" />

declare namespace Cypress {
    interface Chainable {
      getByData(dataTestAttribute: string): Chainable<JQuery<HTMLElement>>
      setup(): void
    }
  }
  
  Cypress.Commands.add("getByData", (selector) => {
    return cy.get(`[data-test=${selector}]`)
  })

  // Before every Test cy.reset() should be called to ensure Tests run independent
  Cypress.Commands.add('setup', () => {
    cy.task('db:reseed')
    cy.clearCookies()
    cy.clearLocalStorage()
  })