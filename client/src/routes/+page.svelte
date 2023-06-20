<script>
	import Aside from '$lib/components/Aside/Aside.svelte';
	import TextField from '$lib/components/TextField.svelte';
</script>

<Aside />
<main class="grid xl:grid-cols-5 gap-4 p-4 sm:ml-64">
	<div class="xl:col-span-2 h-96">
		<form>
			<TextField name="gender" type="text" label="Gender" />
		</form>
	</div>
	<div class="xl:col-span-3 bg-slate-700 h-96">02</div>
	<div class="xl:col-span-3 bg-slate-700 h-96">04</div>
	<div class="xl:col-span-2 bg-slate-700 h-96">05</div>
</main>

<!-- genero, peso, altura, edad, actividad_level -->
