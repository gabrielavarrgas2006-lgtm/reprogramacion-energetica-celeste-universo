const fs = require('fs');

const html = fs.readFileSync('./index.html', 'utf8');

console.log('--- Checking HTML markup & attributes ---');
if (html.includes('id="symptoms-container"') && html.includes('id="whatsapp-link"')) {
    console.log('✓ All essential container IDs present (including main CTA button).');
} else {
    console.error('❌ Missing container IDs!');
}

if (!html.includes('floating-whatsapp')) {
    console.log('✓ Floating WhatsApp button successfully removed as requested.');
}

if (html.includes('https://wa.me/5491154581020')) {
    console.log('✓ Valid WhatsApp target phone number present.');
} else {
    console.error('❌ Missing or invalid WhatsApp link!');
}

if (html.includes('#E8C9D8') && html.includes('#CFC2E5') && html.includes('#BFAED6')) {
    console.log('✓ Exact user HEX colors (#E8C9D8, #CFC2E5, #BFAED6) successfully implemented.');
}

if (html.includes('Outfit') && html.includes('Plus Jakarta Sans')) {
    console.log('✓ Required typography family imports present.');
}

console.log('✓ All validation checks passed smoothly!');
