// Mobile Menu Toggle
const openMenu = document.getElementById("openMenu");
const closeMenu = document.getElementById("closeMenu");
const mobileMenu = document.getElementById("mobileMenu");
const navbar = document.getElementById("navbar");

openMenu.addEventListener("click", () => {
    mobileMenu.classList.remove("-translate-x-full");
    document.body.classList.add("overflow-hidden");
    navbar.classList.remove("backdrop-blur");
});

closeMenu.addEventListener("click", () => {
    mobileMenu.classList.add("-translate-x-full");
    document.body.classList.remove("overflow-hidden");
    navbar.classList.add("backdrop-blur");
});

// Close mobile menu when clicking on links
mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.add("-translate-x-full");
        document.body.classList.remove("overflow-hidden");
        navbar.classList.add("backdrop-blur");
    });
});

// Timeline / Alur Pendaftaran Data
const timelineData = [
    {
        step: 1,
        icon: `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" class="text-purple-500 size-8"><path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><polyline points="10 17 15 12 10 7"/><line x1="15" x2="3" y1="12" y2="12"/></svg>`,
        title: "Registrasi Online",
        description: "Isi formulir pendaftaran online dengan data diri lengkap dan akurat.",
    },
    {
        step: 2,
        icon: `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" class="text-purple-500 size-8"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M12 18v-6"/><path d="m9 15 3 3 3-3"/></svg>`,
        title: "Upload Berkas",
        description: "Unggah dokumen persyaratan sesuai dengan ketentuan yang berlaku.",
    },
    {
        step: 3,
        icon: `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" class="text-purple-500 size-8"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="m9 12 2 2 4-4"/></svg>`,
        title: "Verifikasi Data",
        description: "Tim kami akan memverifikasi kelengkapan dan kebenaran data Anda.",
    },
    {
        step: 4,
        icon: `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" class="text-purple-500 size-8"><path d="m22 8-6 4 6 4V8Z"/><rect width="14" height="12" x="2" y="6" rx="2" ry="2"/></svg>`,
        title: "Pengumuman",
        description: "Hasil seleksi akan diumumkan melalui website dan notifikasi email.",
    },
];

const timeline = document.getElementById("timeline");
timeline.innerHTML = timelineData.map((item, index) => `
    <div class="flex items-center">
        <!-- Step Card -->
        <div class="flex flex-col items-center text-center w-44 md:w-52 px-3">
            <!-- Step Number Circle -->
            <div class="flex items-center justify-center size-14 md:size-16 rounded-full bg-gradient-to-br from-purple-600 to-violet-600 text-white font-bold text-lg md:text-xl shadow-lg shadow-purple-500/30 mb-4">
                ${item.step}
            </div>
            <!-- Icon -->
            <div class="flex items-center justify-center size-12 rounded-xl bg-purple-500/10 mb-3">
                ${item.icon}
            </div>
            <!-- Title -->
            <h3 class="text-sm md:text-base font-semibold text-white mb-2">${item.title}</h3>
            <!-- Description -->
            <p class="text-xs md:text-sm text-slate-400 leading-relaxed">${item.description}</p>
        </div>
        <!-- Connector Line -->
        ${index < timelineData.length - 1 ? `
            <div class="flex items-center justify-center w-8 md:w-16 -mt-20">
                <div class="h-0.5 w-full bg-gradient-to-r from-purple-500 to-violet-500"></div>
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-purple-500 shrink-0 -ml-1">
                    <path d="m9 18 6-6-6-6"/>
                </svg>
            </div>
        ` : ''}
    </div>
`).join("");

// Biaya / Pricing Data
const biayaData = [
    {
        title: "Biaya Pendaftaran",
        price: "250.000",
        period: "sekali bayar",
        features: [
            "Formulir Pendaftaran",
            "Tes Seleksi Masuk",
            "Seragam Olahraga",
            "Buku Panduan Siswa",
            "Kartu Pelajar",
        ],
        buttonText: "Daftar Sekarang",
    },
    {
        title: "SPP Bulanan",
        price: "500.000",
        period: "per bulan",
        mostPopular: true,
        features: [
            "Biaya Pendidikan",
            "Kegiatan Ekstrakurikuler",
            "Bimbingan Belajar",
            "Fasilitas Perpustakaan",
            "Akses E-Learning",
            "Kegiatan Praktikum",
        ],
        buttonText: "Info Selengkapnya",
    },
    {
        title: "Biaya Tahunan",
        price: "1.500.000",
        period: "per tahun",
        features: [
            "Dana Pengembangan",
            "Kegiatan Study Tour",
            "Asuransi Siswa",
            "Yearbook & Dokumentasi",
            "Event Sekolah",
        ],
        buttonText: "Info Selengkapnya",
    },
];

const pricingContainer = document.getElementById("pricing");

pricingContainer.innerHTML = biayaData.map(plan => `
      <div class="p-6 rounded-2xl max-w-75 w-full shadow-[0px_4px_26px] shadow-black/6 
        ${plan.mostPopular
        ? "relative pt-12 bg-gradient-to-b from-indigo-600 to-violet-600 text-white"
        : "bg-white/50 dark:bg-gray-800/50 border border-slate-200 dark:border-slate-800"}">

        ${plan.mostPopular
        ? `<div class="flex items-center text-xs gap-1 py-1.5 px-2 text-purple-600 absolute top-4 right-4 rounded bg-white font-medium">
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-sparkles-icon lucide-sparkles"><path d="M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z"/><path d="M20 2v4"/><path d="M22 4h-4"/><circle cx="4" cy="20" r="2"/></svg>
              <p>Terpopuler</p>
            </div>`
        : ""}

        <p class="font-medium ${plan.mostPopular ? "text-white" : ""}">${plan.title}</p>
        <h4 class="text-3xl font-semibold mt-1 ${plan.mostPopular ? "text-white" : ""}">
          Rp ${plan.price}<span class="font-normal text-sm ${plan.mostPopular ? "text-white/80" : "text-slate-400"}">${plan.period ? `/${plan.period}` : ''}</span>
        </h4>

        <hr class="my-8 ${plan.mostPopular ? "border-gray-300" : "border-slate-300 dark:border-slate-700"}" />

        <div class="space-y-2 ${plan.mostPopular ? "text-white" : "text-slate-600 dark:text-slate-300"}">
          ${plan.features.map(f => `
            <div class="flex items-center gap-1.5">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="${plan.mostPopular ? "text-white" : "text-purple-600"}"><path d="M20 6 9 17l-5-5"/></svg>
              <span>${f}</span>
            </div>
          `).join("")}
        </div>

        <button class="transition w-full py-3 rounded-lg font-medium mt-8 
          ${plan.mostPopular
        ? "bg-white hover:bg-slate-100 text-slate-800"
        : "bg-purple-600 hover:bg-purple-700 text-white"}">
          ${plan.buttonText}
        </button>
      </div>
    `).join("");

// FAQ Data
const faqsData = [
    {
        question: "Kapan jadwal pendaftaran siswa baru dibuka?",
        answer: "Pendaftaran siswa baru untuk tahun ajaran 2025/2026 dibuka mulai tanggal 1 Januari hingga 31 Maret 2025. Pastikan mendaftar sebelum kuota terpenuhi."
    },
    {
        question: "Apa saja persyaratan untuk mendaftar?",
        answer: "Persyaratan utama meliputi: fotokopi akta kelahiran, kartu keluarga, ijazah/SKHUN terakhir, pas foto 3x4 sebanyak 4 lembar, surat keterangan sehat, dan fotokopi KTP orang tua/wali."
    },
    {
        question: "Bagaimana cara mendaftar secara online?",
        answer: "Klik tombol 'Daftar Sekarang', isi formulir pendaftaran dengan lengkap, upload dokumen yang diperlukan, dan lakukan pembayaran biaya pendaftaran. Anda akan menerima email konfirmasi setelah pendaftaran berhasil."
    },
    {
        question: "Kapan pengumuman hasil seleksi?",
        answer: "Pengumuman hasil seleksi akan diumumkan 2 minggu setelah periode pendaftaran ditutup. Hasil dapat dilihat melalui website resmi atau melalui email yang terdaftar."
    },
    {
        question: "Apakah ada beasiswa untuk siswa berprestasi?",
        answer: "Ya, kami menyediakan program beasiswa untuk siswa berprestasi baik di bidang akademik maupun non-akademik. Informasi lebih lanjut dapat ditanyakan saat proses pendaftaran."
    },
    {
        question: "Bagaimana jika mengalami kendala saat pendaftaran?",
        answer: "Jika mengalami kendala, silakan hubungi tim helpdesk kami melalui WhatsApp di +62 812-3456-7890 atau email ke psb@sekolah.sch.id. Kami siap membantu Anda."
    }
];

const faqContainer = document.getElementById("faq-container");

faqContainer.innerHTML = faqsData.map((faq, index) => `
      <div class="border-b border-slate-300 dark:border-purple-900 py-4 cursor-pointer w-full" data-index="${index}">
        <div class="flex items-center justify-between">
          <h3 class="text-base font-medium pr-4">${faq.question}</h3>
          <!-- ChevronDown icon placeholder -->
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-4 h-4 transition-transform duration-500 ease-in-out shrink-0" data-chevron><path d="m6 9 6 6 6-6"/></svg>
        </div>
        <p class="faq-answer text-sm text-slate-600 dark:text-slate-300 transition-all duration-500 ease-in-out max-w-xl opacity-0 max-h-0 overflow-hidden -translate-y-2">
          ${faq.answer}
        </p>
      </div>
    `).join("");

// Accordion Logic
const faqItems = document.querySelectorAll("#faq-container > div");

faqItems.forEach(item => {
    const chevron = item.querySelector("[data-chevron]");
    const answer = item.querySelector(".faq-answer");

    item.addEventListener("click", () => {
        const isOpen = answer.classList.contains("opacity-100");

        // Close all
        faqItems.forEach(i => {
            i.querySelector(".faq-answer").classList.remove("opacity-100", "max-h-[500px]", "translate-y-0", "pt-4");
            i.querySelector(".faq-answer").classList.add("opacity-0", "max-h-0", "-translate-y-2");
            i.querySelector("[data-chevron]").classList.remove("rotate-180");
        });

        // Toggle current
        if (!isOpen) {
            answer.classList.add("opacity-100", "max-h-[500px]", "translate-y-0", "pt-4");
            answer.classList.remove("opacity-0", "max-h-0", "-translate-y-2");
            chevron.classList.add("rotate-180");
        }
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});