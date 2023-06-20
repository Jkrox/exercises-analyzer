<script lang="ts">
	import { onMount } from 'svelte';

	export let href: string;
	let active: boolean;
	onMount(() => {
		active = window.location.pathname == href;
	});
</script>

<li>
	<a
		{href}
		class="flex items-center p-2 text-black rounded-lg hover:bg-red-100"
		class:bg-red-100={active}
	>
		<slot />
	</a>
</li>
