// ==========================================
// API Types
// ==========================================

export interface UserProfile {
  full_name?: string
  bio?: string
  avatar_url?: string
}

export interface UserTheme {
  background_color: string
  button_style: string
  button_color: string
  font_family: string
}

export interface User {
  id: string
  username: string
  email: string
  profile: UserProfile
  theme: UserTheme
  tier: 'free' | 'pro' | 'business'
  is_active: boolean
  email_verified: boolean
  created_at: string
  updated_at: string
}

export interface AuthResponse {
  access_token: string
  refresh_token: string
  token_type: string
  expires_in: number
  user?: User
}

export interface Link {
  id: string
  title: string
  url: string
  type: 'standard' | 'affiliate_product'
  image_url: string | null
  sort_order: number
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface CreateLinkRequest {
  title: string
  url: string
  type?: 'standard' | 'affiliate_product'
  image_url?: string | null
}

export interface UpdateLinkRequest {
  title?: string
  url?: string
  type?: 'standard' | 'affiliate_product'
  image_url?: string | null
  sort_order?: number
  is_active?: boolean
}

export interface ReorderItem {
  id: string
  sort_order: number
}

export interface ReorderLinksRequest {
  items: ReorderItem[]
}

export interface UpdateProfileRequest {
  full_name?: string
  bio?: string
  avatar_url?: string
  background_color?: string
  button_style?: 'rounded' | 'pill' | 'soft'
  button_color?: string
  font_family?: string
}

export interface BioData {
  username: string
  profile: UserProfile
  theme: UserTheme
  links: Link[]
  tier: string
}

export interface TrackViewPayload {
  username: string
  referrer: string
  user_agent: string
  device: string
}

export interface TrackClickPayload {
  username: string
  link_id: string
  timestamp: string
  page_url: string
}

export interface AnalyticsSummary {
  total_views: number
  total_clicks: number
  daily_stats: Array<{
    date: string
    views: number
    clicks: number
  }>
  links_stats: Array<{
    link_id: string
    title: string
    clicks: number
  }>
}
