/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // KunLun Terminal Pro — Custom Palette
        kunlun: {
          bg:      '#0D1117',    // Deep space background
          surface: '#161B22',    // Card / panel surface
          border:  '#30363D',    // Subtle borders
          text:    '#E6EDF3',    // Primary text
          muted:   '#8B949E',    // Secondary text
          cyan:    '#00F5FF',    // Primary accent
          magenta: '#FF00FF',    // Secondary accent
          purple:  '#A855F7',    // Tertiary
          up:      '#EF4444',    // 红涨 (Red = Up, Chinese convention)
          down:    '#22C55E',    // 绿跌 (Green = Down, Chinese convention)
        },
      },
      fontFamily: {
        mono:  ['JetBrains Mono', 'Fira Code', 'monospace'],
        sans:  ['Inter', 'system-ui', 'sans-serif'],
      },
      backdropBlur: {
        glass: '20px',
      },
    },
  },
  plugins: [],
}
