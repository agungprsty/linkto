<template>
  <footer class="bg-black pt-20 pb-10 text-white">
    <div class="max-w-screen-2xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 md:grid-cols-5 gap-10 mb-16">
        <!-- Brand -->
        <div class="col-span-2 md:col-span-2">
          <NuxtLink to="/" class="flex items-center gap-2 mb-6">
            <div class="w-10 h-10 bg-brand-yellow border-2 border-brand-yellow rounded-full flex items-center justify-center text-black">
              <Icon name="ph:link" class="text-2xl font-bold" />
            </div>
            <span class="font-black text-4xl">Linkto.</span>
          </NuxtLink>
          <p class="font-semibold text-gray-400 text-lg max-w-sm">The only bio link you'll ever need. Designed for creators, built for conversion.</p>
          <div class="flex gap-3 mt-6">
            <a href="#" class="w-10 h-10 bg-gray-800 flex items-center justify-center rounded-full hover:bg-brand-blue hover:text-black transition-colors" aria-label="Twitter">
              <Icon name="ph:twitter-logo" class="text-xl" />
            </a>
            <a href="#" class="w-10 h-10 bg-gray-800 flex items-center justify-center rounded-full hover:bg-brand-pink hover:text-black transition-colors" aria-label="Instagram">
              <Icon name="ph:instagram-logo" class="text-xl" />
            </a>
            <a href="#" class="w-10 h-10 bg-gray-800 flex items-center justify-center rounded-full hover:bg-white hover:text-black transition-colors" aria-label="TikTok">
              <Icon name="ph:tiktok-logo" class="text-xl" />
            </a>
            <a href="#" class="w-10 h-10 bg-gray-800 flex items-center justify-center rounded-full hover:bg-brand-yellow hover:text-black transition-colors" aria-label="YouTube">
              <Icon name="ph:youtube-logo" class="text-xl" />
            </a>
          </div>
        </div>

        <!-- Product -->
        <div>
          <h4 class="font-black text-xl mb-6 text-brand-pink">Product</h4>
          <ul class="space-y-4 font-semibold text-gray-300">
            <li><a href="/#features" class="hover:text-white transition-colors">Features</a></li>
            <li><a href="/#pricing" class="hover:text-white transition-colors">Pricing</a></li>
            <li><a href="#" class="hover:text-white transition-colors">Affiliate Hub</a></li>
            <li><a href="#" class="hover:text-white transition-colors">Custom Domain</a></li>
            <li><a href="/templates" class="hover:text-white transition-colors">Templates</a></li>
          </ul>
        </div>

        <!-- Resources -->
        <div>
          <h4 class="font-black text-xl mb-6 text-brand-blue">Resources</h4>
          <ul class="space-y-4 font-semibold text-gray-300">
            <li><NuxtLink to="/blog" class="hover:text-white transition-colors">Blog</NuxtLink></li>
            <li><NuxtLink to="/help" class="hover:text-white transition-colors">Help Center</NuxtLink></li>
            <li><NuxtLink to="/community" class="hover:text-white transition-colors">Community</NuxtLink></li>
            <li><a href="#" class="hover:text-white transition-colors">API Docs</a></li>
            <li><a href="#" class="hover:text-white transition-colors">Status Page</a></li>
          </ul>
        </div>

        <!-- Company -->
        <div>
          <h4 class="font-black text-xl mb-6 text-brand-green">Company</h4>
          <ul class="space-y-4 font-semibold text-gray-300">
            <li><NuxtLink to="/about" class="hover:text-white transition-colors">About Us</NuxtLink></li>
            <li><a href="#" class="hover:text-white transition-colors">Careers</a></li>
            <li><NuxtLink to="/privacy" class="hover:text-white transition-colors">Privacy Policy</NuxtLink></li>
            <li><NuxtLink to="/terms" class="hover:text-white transition-colors">Terms of Service</NuxtLink></li>
            <li><NuxtLink to="/cookie" class="hover:text-white transition-colors">Cookie Policy</NuxtLink></li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="border-t-4 border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="font-bold text-gray-500">© {{ new Date().getFullYear() }} Linkto Inc. All rights reserved.</p>
        <div class="flex gap-6 text-sm font-bold text-gray-500">
          <NuxtLink to="/privacy" class="hover:text-white transition-colors">Privacy Policy</NuxtLink>
          <NuxtLink to="/terms" class="hover:text-white transition-colors">Terms of Service</NuxtLink>
          <NuxtLink to="/cookie" class="hover:text-white transition-colors">Cookie Settings</NuxtLink>
        </div>
      </div>
    </div>
  </footer>
</template>
