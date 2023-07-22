const baseUrl = 'http://localhost:5173/new_challenge/RenameColumn';
describe('RenameColumn Test', () => {
    it('Confirm pandas import in CodeEditor', () => {
        cy.visit(baseUrl)
        cy.get('.cm-line').should('contain', 'import pandas as pd');
    })
  })