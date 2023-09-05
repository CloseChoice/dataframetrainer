/// <reference types="cypress" />

declare namespace Cypress {
    interface Chainable {
      getByData(dataTestAttribute: string, options?: Partial<Loggable & Timeoutable & Withinable & Shadow>): Chainable<JQuery<HTMLElement>>
      setup(): void
    }
  }
  
  Cypress.Commands.add("getByData", (selector, options = {}) => {
    return cy.get(`[data-test=${selector}]`, options)
  })

  // Before every Test cy.reset() should be called to ensure Tests run independent
  Cypress.Commands.add('setup', () => {
    cy.task('db:reseed')
    cy.clearCookies()
    cy.clearLocalStorage()
  })