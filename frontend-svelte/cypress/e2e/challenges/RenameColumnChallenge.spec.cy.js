// cypress/integration.giftcards/giftcards.spec.js

const baseUrl = 'http://localhost:5173/new_challenge/RenameColumn';
describe('RenameColumn Test', () => {
    it('Confirms gift card data', () => {
        cy.visit(baseUrl)
        cy.get('#firstEdIntro').invoke('prop', 'innerText').should('contain', 'import pandas as pd');
    })
  })