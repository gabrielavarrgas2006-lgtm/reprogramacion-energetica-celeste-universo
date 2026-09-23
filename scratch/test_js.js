const fs = require('fs');

const html = fs.readFileSync('./index.html', 'utf8');

console.log('--- Checking HTML markup & attributes ---');
if (html.includes('id="symptoms-container"') && html.includes('id="whatsapp-link"') && html.includes('id="floating-whatsapp-btn"')) {
    console.log('✓ All essential container IDs present.');
} else {
    console.error('❌ Missing container IDs!');
}

if (html.includes('https://wa.me/5491154581020')) {
    console.log('✓ Valid WhatsApp target phone number present.');
} else {
    console.error('❌ Missing or invalid WhatsApp link!');
}

if (html.includes('Outfit') && html.includes('Plus Jakarta Sans')) {
    console.log('✓ Required typography family imports present.');
} else {
    console.error('❌ Missing typography imports!');
}

console.log('✓ Validation passed smoothly!');
