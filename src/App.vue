<template>
  <div class="h-screen bg-amber-50 flex flex-col items-center justify-center px-4 py-12">
    <div class="text-center mb-12 animate-bounce">
      <span class="text-6xl mb-2 inline-block">🧀</span>
    </div>

    <h1 class="text-4xl md:text-5xl font-bold text-amber-600 mb-12 tracking-wider">
      奶酪大盗
    </h1>

    <div class="flex flex-col gap-6 w-full max-w-xs">
      <button
          class="bg-amber-400 hover:bg-amber-500 text-amber-900 font-bold py-4 px-6 rounded-xl shadow-lg transform transition-all duration-300 hover:scale-105 active:scale-95 text-xl"
          @click="playing ? stop() : start()"
      >
        {{ playing ? '重置游戏' : '开始游戏' }}
      </button>
    </div>

    <div class="mt-12 text-amber-700 text-sm">
      XSD © 2025
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue';

const playing = ref(false)

const playAudio = () => {
  return new Promise((resolve) => {
    const audio = new Audio(`./audio.mp3`)
    audio.onended = resolve
    audio.play()
  })
}

const start = () => {
  if (playing.value) return
  playing.value = true
  playAudio().finally(() => playing.value = false)
}

const stop = () => {
  window.location.reload()
}

</script>
