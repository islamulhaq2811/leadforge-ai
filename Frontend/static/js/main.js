// ===== Sticky Navbar =====
const navbar = document.getElementById('navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    if (currentScroll > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
    lastScroll = currentScroll;
});

// ===== Mobile Menu =====
const menuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

menuBtn?.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
});

// Close mobile menu on link click
mobileMenu?.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
    });
});

// ===== Scroll Animations (Intersection Observer) =====
const animateElements = () => {
    const elements = document.querySelectorAll(
        '.service-card, .project-card, .process-step, .stat-item, .testimonial-card, ' +
        '#about h2, #about p, .glass-card, #pricing .rounded-2xl, #contact h2'
    );

    elements.forEach(el => {
        el.classList.add('fade-in');
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    elements.forEach(el => observer.observe(el));
};

document.addEventListener('DOMContentLoaded', animateElements);

// ===== Image Preview Modal =====
const imageModal = document.getElementById('image-modal');
const imageModalImg = document.getElementById('image-modal-img');
const imageModalCaption = document.getElementById('image-modal-caption');
const imageModalClose = document.getElementById('image-modal-close');

function openImageModal(src, title) {
    imageModalImg.src = src;
    imageModalCaption.textContent = title;
    imageModal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeImageModal() {
    imageModal.classList.remove('active');
    document.body.style.overflow = '';
}

imageModalClose?.addEventListener('click', closeImageModal);
imageModal?.addEventListener('click', (e) => {
    if (e.target === imageModal) closeImageModal();
});

// Click handlers for portfolio image previews
document.addEventListener('click', (e) => {
    const trigger = e.target.closest('.image-preview-trigger');
    if (trigger) {
        const src = trigger.dataset.src;
        const title = trigger.dataset.title;
        openImageModal(src, title);
    }
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeImageModal();
        closeModal();
    }
});

// ===== Case Study Modal =====
const modal = document.getElementById('case-study-modal');
const modalTitle = document.getElementById('modal-title');
const modalBody = document.getElementById('modal-body');
const modalClose = document.getElementById('modal-close');

const caseStudies = {
    'AI Customer Support Chatbot': 'This AI-powered chatbot was built for a high-growth SaaS company handling 10,000+ customer inquiries monthly. Using GPT-4 fine-tuned on their knowledge base, it achieved 90% first-response resolution rate. The system integrates with Zendesk, Slack, and their internal CRM, reducing support team workload by 70%.',
    'Invoice Automation System': 'An end-to-end invoice processing automation for a mid-size accounting firm. The system uses OCR + AI to extract data from PDF invoices, validates against purchase orders, routes for approval, and triggers payments. Processing time dropped from 45 minutes to under 3 minutes per invoice.',
    'Real-Time Analytics Dashboard': 'Built for a series of early-stage startups needing live KPI tracking. The dashboard pulls from multiple data sources (Stripe, Google Analytics, social platforms) and provides AI-generated insights and recommendations. Three startups currently use it for daily decision-making.',
    'Multi-Vendor E-Commerce': 'A scalable marketplace platform connecting vendors with customers. Features include automated vendor onboarding, commission tracking, payment splitting, inventory management across warehouses, and AI-powered product recommendations. Currently processing 5,000+ orders monthly.',
};

document.querySelectorAll('.case-study-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const projectName = btn.dataset.project;
        modalTitle.textContent = projectName;
        modalBody.textContent = caseStudies[projectName] || 'Case study details coming soon.';
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    });
});

modalClose?.addEventListener('click', closeModal);
modal?.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
});

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeModal();
});

function closeModal() {
    modal?.classList.remove('active');
    document.body.style.overflow = '';
}

// ===== Contact Form =====
const contactForm = document.getElementById('contact-form');

contactForm?.addEventListener('submit', (e) => {
    e.preventDefault();

    const formData = new FormData(contactForm);
    const data = Object.fromEntries(formData.entries());
    console.log('Form submitted:', data);

    const toast = document.createElement('div');
    toast.className = 'toast show';
    toast.textContent = '✓ Thank you! We\'ll be in touch within 24 hours.';
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 400);
    }, 4000);

    contactForm.reset();
});
