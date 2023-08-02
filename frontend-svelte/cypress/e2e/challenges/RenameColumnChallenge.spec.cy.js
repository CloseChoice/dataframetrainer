
describe('RenameColumn Test', () => {
    it('Confirm pandas import in CodeEditor', () => {
        cy.visit('/new_challenge/RenameColumn')
        cy.get('.cm-line').should('contain', 'import pandas as pd');
    })
  })