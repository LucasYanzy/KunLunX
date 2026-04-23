<template>
  <el-config-provider :locale="zhCn">
    <TerminalLayout />
  </el-config-provider>
</template>

<script setup lang="ts">
import { ElConfigProvider } from 'element-plus'
import zhCn from 'element-plus/es/locale/lang/zh-cn'
import TerminalLayout from '@/layouts/TerminalLayout.vue'
</script>
