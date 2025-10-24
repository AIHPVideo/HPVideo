<script lang="ts">
	import { getContext } from 'svelte';
	import { mobile } from "$lib/stores";
	const i18n = getContext('i18n');
	export let videourl = "";
</script>

<div class="w-full mt-3 mb-4">
	<div class="flex w-full">
		<div class="w-full {$mobile ? '' : 'max-w-[600px]'}">
			<video class="my-1 rounded-lg bg-red" controls src={videourl} width="800"/>
		</div>
	</div>
</div>