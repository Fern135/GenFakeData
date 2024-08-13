const { faker } = require('@faker-js/faker');

class DataGenerator {
    static generateUsers(count) {
        const users = [];
        for (let i = 0; i < count; i++) {
            users.push({
                id: i + 1,
                str_id: faker.string.uuid(), 
                name: faker.name.fullName(),
                email: faker.internet.email(),
                phone: faker.phone.number(),
            });
        }
        return users;
    }

    static generateProducts(count) {
        const products = [];
        for (let i = 0; i < count; i++) {
            products.push({
                id: i + 1,
                str_id: faker.string.uuid(), 
                name: faker.commerce.productName(),
                price: faker.commerce.price(),
                category: faker.commerce.department(),
            });
        }
        return products;
    }

    static generateCompanies(count) {
        const companies = [];
        for (let i = 0; i < count; i++) {
            companies.push({
                id: i + 1,
                str_id: faker.string.uuid(), 
                name: faker.company.name(),
                catchPhrase: faker.company.catchPhrase(),
                industry: faker.commerce.department(), // Use faker.commerce.department() as a workaround
            });
        }
        return companies;
    }

    static generateCreditCards(count) {
        const creditCards = [];
        const cardTypes = ['Visa', 'MasterCard', 'American Express', 'Discover'];
        
        for (let i = 0; i < count; i++) {
            creditCards.push({
                id: i + 1,
                str_id: faker.string.uuid(), 
                number: faker.finance.creditCardNumber(), 
                type: cardTypes[Math.floor(Math.random() * cardTypes.length)],
                // expDate: faker.date.future(5).toISOString().split('T')[0], 
                expDate: faker.date.future({ years: 5, refDate: new Date() }),
            });
        }
        return creditCards;
    }

    static generateJobs(count) {
        const jobs = [];
        for (let i = 0; i < count; i++) {
            jobs.push({
                id: i + 1,
                str_id: faker.string.uuid(), 
                title: faker.name.jobTitle(),
                company: faker.company.name(),
                location: faker.address.city(),
            });
        }
        return jobs;
    }

    static generateTextContents(count) {
        const contents = [];
        for (let i = 0; i < count; i++) {
            contents.push({
                id: i + 1,
                str_id: faker.string.uuid(), 
                text: faker.lorem.paragraph(),
            });
        }
        return contents;
    }
}

module.exports = DataGenerator;
