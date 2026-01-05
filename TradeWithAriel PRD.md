# TradeWithAriel – Product Requirements Document (PRD)

## 1. Product Overview
**Product Name:** TradeWithAriel  
**Product Type:** Single-page marketing & trust website for trading brand  
**Purpose:** Present TradeWithAriel as a premium, trustworthy, institutional-grade trading platform/brand that signals credibility, clarity, and financial authority.

TradeWithAriel will be a **single HTML page (SPA-style, no page reloads)** where all navigation scrolls smoothly to sections within the same page.

---

## 2. Goals & Objectives
### Primary Goals
- Establish **trust and legitimacy** (institutional-grade feel)
- Clearly communicate **value proposition** within 5 seconds
- Convert visitors into **leads, subscribers, or clients**

### Success Metrics (KPIs)
- Time on page > 2 minutes
- Bounce rate < 45%
- CTA click-through rate
- Lead conversion rate

---

## 3. Target Audience
- Beginner to intermediate traders
- Retail traders seeking structure & mentorship
- Users skeptical of "get-rich-quick" schemes

### Audience Expectations
- Clean, professional UI (bank / fintech level)
- No clutter, no hype
- Fast load time
- Clear explanations

---

## 4. Design & UI Requirements
### Design Philosophy
- **Sleek, modern, institutional-grade**
- Inspired by banks, hedge funds, fintech dashboards
- Premium but minimal

### Color Scheme
- Primary: **Green** (wealth, growth, money)
- Secondary: **White** (clarity, trust)
- Accents: Soft dark gray / black for contrast

### Visual Style
- Glassmorphism (glass cards)
- Soft shadows
- Rounded corners
- Subtle gradients
- Smooth animations (not flashy)

### Typography
- Sans-serif, modern font
- Strong hierarchy (Headlines > Subheadings > Body)

---

## 5. Technical Architecture
### Structure
- **Single HTML file**
- All sections stacked vertically
- Navigation links scroll to section IDs

### Navigation Behavior
- No page reloads
- No route changes
- Smooth scroll animation
- Active section highlighted in navbar

### Tech Stack (Initial)
- HTML5
- CSS3 (or Tailwind CSS)
- Vanilla JS or minimal JS

*(Frameworks like React are intentionally avoided for simplicity and speed in v1)*

---

## 6. Website Sections (Same Page)

> All sections live on **one single HTML page**. Navigation scrolls to sections. No page reloads. No routing.

---

### 6.1 Home / Hero Section
**Purpose:** Immediate credibility + emotional proof

**Key Features:**
- Full-width hero section
- **Animated / moving background** using:
  - Screenshots of chats
  - PNL results
  - Trade confirmations
- Background motion must be subtle (slow parallax or horizontal drift)

**Foreground Content:**
- Clear headline explaining TradeWithAriel
- Short authority-driven subtext (not hype)
- Primary CTA (Explore Mentorship / Get Started)

**UI Rules:**
- Glass overlay card on top of background
- Green highlights for CTA
- Background content slightly blurred to avoid distraction

---

### 6.2 Mentorship Section
**Purpose:** Funnel users into specific communities or access points

**Structure:** Glass card grid

**Cards (Editable):**
1. Join Trading Journal
2. Join Nigerian Stock Class
3. Join Personal Trading Channel / Group
4. Connect With Me (Private DMs)

**Admin Editability:**
- Admin can add, remove, or edit mentorship cards
- Editable fields: title, description, destination link

**Behavior:**
- Each card links to an external destination (Telegram, WhatsApp, Discord, etc.)
- Hover states reinforce premium feel

**UI Rules:**
- Equal card sizing
- Icons + short descriptions
- Glassmorphism with clear hierarchy

---

### 6.3 Payments / Marketplace Section
**Purpose:** Monetization hub

**Working Name:** Payments / Marketplace / Offers (final name TBD)

**Functionality:**
- Display purchasable items such as:
  - Discounted prop firm accounts
  - Paid signals
  - Trading tools
  - One-time offers
- Each item displayed as a glass card
- Click → payment flow

**Admin Editability:**
- Fully manageable from custom admin dashboard
- Admin can:
  - Add / remove products
  - Edit price
  - Edit description
  - Upload / replace product images
  - Enable / disable items

**Image Handling:**
- Image uploads must auto-scale and crop safely
- Images must preserve glassmorphism UI without breaking layout

**UI Rules:**
- Clean pricing cards
- Clear CTA buttons
- No clutter or aggressive sales language

---

### 6.4 About Section
**Purpose:** Trust & transparency

**Content:**
- About the owner
- When the channel was created
- Trading background
- Trading style & instruments traded
- Philosophy and risk approach

**Admin Editability:**
- Fully editable from custom admin dashboard
- Text content can be updated without touching code
- Images/screenshots can be replaced or removed

**Visuals:**
- Screenshots (proof, platforms, history)
- Profile or brand imagery

**UI Rules:**
- Structured layout (text + visuals)
- Glass cards for key facts
- Calm, professional tone

---

### 6.5 Contact Section
**Purpose:** Communication & lead capture

**Content:**
- Contact form (name, email, message)
- Email address
- Social media links

**UI Rules:**
- Minimal form fields
- Clear success feedback
- Glass container

---

### 6.6 Navigation Bar
**Behavior:**
- Sticky header
- Smooth scroll to sections

**Menu Items:**
- Home
- Mentorship
- Offers
- About
- Contact

**Extras:**
- Logo placement (left)
- CTA button (right, optional)

---

### 6.7 Footer
**Content:**
- Logo
- Copyright
- Quick links
- Disclaimer (non-financial advice)

**UI Rules:**
- Dark or muted background
- Clean typography

---

## 7. Animations & Interactions
- Smooth scroll
- Subtle background motion
- Hover effects on cards
- Section fade-ins

---

## 8. Performance, Quality & Responsiveness Requirements
- Page load < 2 seconds
- Mobile-first responsive design
- Optimized images (lazy loading)
- Smooth scrolling on all devices
- Touch-friendly UI elements
- Page load < 2 seconds
- Mobile-first
- Optimized images

---

## 9. Constraints & Non-Goals
### Constraints
- Single HTML page
- Minimal JS

### Non-Goals (v1)
- User dashboards
- Auth
- Backend logic

---

## 10. Future Expansion
- Admin dashboard enhancements
- Advanced payments
- Analytics

---

## 11. Admin Dashboard (Custom)

### Purpose
Provide a **simple, low-friction control panel** for 1–2 internal users to update site content quickly. This dashboard prioritizes **clarity and speed over visual polish**.

---

### Tone & Complexity Level
- Functional, not flashy
- Clean and readable
- Less strict than public website UI
- Still responsive, but no heavy animations

---

### Core Design Principles (Non-Negotiable)
- Institutional-grade UI (fintech / bank-level)
- Simple language (no technical jargon)
- Zero risk of breaking frontend layout
- Fully responsive (desktop, tablet, mobile)

---

### Admin Page Structure (Wireframe-Level)

> This is a **low-fidelity functional wireframe**, not a final UI. Everything here is editable and can be simplified further.

---

#### 1. Login Screen
- Basic email + password form
- Plain card layout
- Minimal branding

---

#### 2. Dashboard Home
**Layout:** Simple vertical layout

**Elements:**
- Page title: "Admin Dashboard"
- Buttons / links:
  - Edit About Section
  - Edit Mentorship Section
  - Edit Marketplace

*(No analytics, no charts, no noise)*

---

#### 3. About Section Editor
**Layout:** Form-based page

**Fields:**
- Textarea(s) for content blocks
- Image upload field

**Actions:**
- Save changes
- Preview on site (optional)

---

#### 4. Mentorship Section Editor
**Layout:** List + form

**Features:**
- List of mentorship cards
- Add new card
- Edit existing card
- Delete or disable card

**Fields per Card:**
- Title
- Short description
- Link URL

---

#### 5. Marketplace Editor
**Layout:** Product list + edit form

**Features:**
- Add new product
- Edit product
- Remove / disable product

**Fields:**
- Product name
- Description
- Price
- Image upload (single or multiple)

**Image Rules:**
- Auto-resize on upload
- Preview image before save

---

#### 2. Admin Dashboard Home
**Purpose:** High-level control center

**Components:**
- Welcome message ("Welcome back, Ariel")
- Quick action cards:
  - Edit About Section
  - Manage Mentorship
  - Manage Marketplace
- Status indicators (e.g. "Site Live")

**UI Rules:**
- Card-based layout
- Glassmorphism retained
- No data overload

---

#### 3. About Section Editor
**Editable Fields:**
- Text blocks (bio, philosophy, background)
- Image uploads (profile, screenshots)

**Features:**
- Rich-text editor (simple formatting only)
- Image preview before save
- Save & publish button

**Guardrails:**
- Character limits
- Image size & ratio enforcement

---

#### 4. Mentorship Section Manager
**Editable Fields:**
- Card title
- Short description
- Destination link

**Features:**
- Add / edit / delete mentorship cards
- Reorder cards via drag & drop
- Toggle card visibility

---

#### 5. Marketplace / Offers Manager
**Editable Fields:**
- Product name
- Description
- Price
- Product image(s)

**Image Handling Rules:**
- Auto-resize & crop on upload
- Enforced aspect ratio
- Preview within glass card UI

**Features:**
- Add / edit / disable products
- Image gallery per product
- Clean pricing display preview

---

### Mobile Responsiveness (Admin)
- Fully usable on mobile devices
- Simple single-column layout
- Standard form inputs
- Large save buttons

---

### Backend Architecture

**Recommended Stack:**
- Django backend
- Custom-built admin panel (separate from Django Admin)

**Why:**
- Security
- Full UI control
- Non-technical usability

---

### Non-Editable Areas (Hard Locked)
- Frontend layout
- Glassmorphism styles
- Navigation structure
- Contact form structure

---

### Critical Rule
Admin edits must **never break visual consistency**, responsiveness, or glass UI behavior.

---

---

## 12. Final Notes
TradeWithAriel must **feel institutional, calm, and credible**.

Anything that feels like a hype trading page is a failure.

---

## 11. Final Notes
TradeWithAriel must **feel institutional, calm, and credible**.

Anything that feels like a hype trading page is a failure.

---

**End of PRD**

