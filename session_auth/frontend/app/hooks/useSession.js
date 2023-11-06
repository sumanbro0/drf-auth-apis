import { create } from 'zustand'
import { persist, createJSONStorage } from 'zustand/middleware'

export const useSession = create(
    persist(
        (set, get) => ({
            isAuthenticated: false,
            authenticate: () => set({ isAuthenticated: true }),
            unAuthenticate: () => set({ isAuthenticated: false }),
        }),
        {
            name: 'user',
            storage: createJSONStorage(() => localStorage),
        }
    )
)