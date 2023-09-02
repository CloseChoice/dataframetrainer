describe('Authentication Form', () => {
    it('Register new user and get a new challenge for her', () => {
        cy.setup()
        cy.request('POST', 'http://localhost:5173/testapi/user', {username: 'Hildegard', password: '123456789'})
        cy.visit('/')
        cy.getByData('new-challenge-button').click()
        cy.url().should('include', '/new_challenge')
    })
    }
)