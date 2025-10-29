<script lang="ts">
	import { getContext } from 'svelte';
	import { mobile } from "$lib/stores";
	const i18n = getContext('i18n');
	export let videourl = "";
	export let videosize = "16:9";

	let sizeflag = true;

	$: if(videosize) {
		if (videosize.includes('*')) {
			if (Number(videosize.split('*')[0]) > Number(videosize.split('*')[1])) {
				sizeflag = true;
			} else {
				sizeflag = false;
			}
		} else if (videosize.includes(':')) {
			if (Number(videosize.split(':')[0]) > Number(videosize.split(':')[1])) {
				sizeflag = true;
			} else {
				sizeflag = false;
			}
		} else {
			sizeflag = true;
		}
	}

</script>

<div class="w-full mt-3 mb-4">
	<div class="flex w-full">
		<div class="w-full {$mobile ? '' : sizeflag ? 'max-w-[300px]' : 'max-w-[600px]'}">
			<video class="my-1 rounded-lg bg-red" controls src={videourl} width="800"/>
		</div>
	</div>
</div>