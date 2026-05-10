import { inject } from 'vue'

/** Provided by App.vue — scrolls/opens the right section for header & footer links */
export const siteNavigationKey = Symbol('siteNavigation')

/**
 * @returns {(hash: string) => void}
 */
export function useSiteNavigation() {
  const navigate = inject(siteNavigationKey, null)
  if (typeof navigate !== 'function') {
    return (hash) => {
      const el = document.querySelector(hash.startsWith('#') ? hash : `#${hash}`)
      el?.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }
  return navigate
}
