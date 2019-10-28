<template>
    <mdb-navbar color="warning" light>
        <!-- Logo -->
        <mdb-navbar-brand href="/">
            <img src="../assets/logo.png" alt="Website logo" height="30">
        </mdb-navbar-brand>
        <!-- Navbar Toggler  -->
        <mdb-navbar-toggler>
            <mdb-navbar-nav>
                <mdb-nav-item exact to="/">Home</mdb-nav-item>
                <mdb-nav-item to="/about">About</mdb-nav-item>
                <mdb-nav-item to="/pinterest">Pinterest</mdb-nav-item>
                <mdb-dropdown tag="li" class="nav-item">
                    <mdb-dropdown-toggle tag="a" navLink color="warning" slot="toggle" waves-fixed>Others</mdb-dropdown-toggle>
                    <mdb-dropdown-menu>
                        <mdb-dropdown-item>Action</mdb-dropdown-item>
                        <mdb-dropdown-item>Another action</mdb-dropdown-item>
                        <mdb-dropdown-item>Something else here</mdb-dropdown-item>
                    </mdb-dropdown-menu>
                </mdb-dropdown>
            </mdb-navbar-nav>
            <form>
                <mdb-input type="text" class="text-white" placeholder="Search" aria-label="Search" label navInput waves waves-fixed/>
            </form>
        </mdb-navbar-toggler>
    </mdb-navbar>
</template>

<script>
import { mdbNavbar, mdbNavbarBrand, mdbNavbarToggler, mdbNavbarNav, mdbNavItem, mdbDropdown, mdbDropdownMenu, mdbDropdownToggle, mdbInput, mdbDropdownItem } from 'mdbvue'
export default {
    name: "Header",
    components: {
        mdbNavbar,
        mdbNavbarBrand,
        mdbNavbarToggler,
        mdbNavbarNav,
        mdbNavItem,
        mdbDropdown,
        mdbDropdownMenu,
        mdbDropdownToggle,
        mdbDropdownItem,
        mdbInput
    }
}
</script>
