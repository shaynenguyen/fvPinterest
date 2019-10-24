<template>
    <!-- Footer -->
    <mdb-footer color="blue-grey" class="page-footer font-small lighten-5 mt-0" styles="margin-top: 0 !important;">
        <div style="backgroundColor: #21d192">
            <!-- Footer Section 1 -->
            <mdb-container class="text-left">
                <mdb-row class="py-4 d-flex align-items-center">
                    <mdb-col md="6" lg="5" class="text-center text-md-left mb-4 mb-md-0">
                        <h6 class="mb-0 white-text">Get connected with us on social networks!</h6>
                    </mdb-col>
                    <mdb-col md="6" lg="7" class="text-center text-md-right">
                        <a class="fb-ic ml-0"><i class="fab fa-facebook white-text mr-lg-4 mr-sm-4"> </i></a>
                        <a class="tw-ic"><i class="fab fa-twitter white-text mr-lg-4 mr-sm-4"> </i></a>
                        <a class="gplus-ic"><i class="fab fa-google-plus white-text mr-lg-4 mr-sm-4"> </i></a>
                        <a class="li-ic"><i class="fab fa-linkedin-in white-text mr-lg-4 mr-sm-4"> </i></a>
                        <a class="ins-ic"><i class="fab fa-instagram white-text mr-lg-4 mr-sm-4"> </i></a>
                    </mdb-col>
                </mdb-row>
            </mdb-container>
        </div>
        <!-- Footer Section 2 -->
        <mdb-container class="mt-5 mb-4 text-center text-md-left">
            <mdb-row class="mt-3">
                <mdb-col md="3" lg="4" xl="4" class="mb-4 dark-grey-text">
                <h6 class="text-uppercase font-weight-bold"><strong>fvPinterest.com</strong></h6>
                <hr class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style="width: 60px" />
                <p>Here you can use rows and columns here to organize your footer content. Lorem ipsum dolor sit
                    amet, consectetur adipisicing elit. Here you can use rows and columns here to organize your footer content. Lorem ipsum dolor sit
                    amet, consectetur adipisicing elit. </p>
                </mdb-col>
                <mdb-col md="2" lg="2" xl="2" class="mb-4 dark-grey-text">
                <h6 class="text-uppercase font-weight-bold"><strong>Backbones</strong></h6>
                <hr class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style="width: 60px" />
                <p><a href="#!" class="dark-grey-text">pythonFlask</a></p>
                <p><a href="#!" class="dark-grey-text">VueJS</a></p>
                <p><a href="#!" class="dark-grey-text">MDBootraps</a></p>
                <p><a href="#!" class="dark-grey-text">Pexels</a></p>
                </mdb-col>
                <mdb-col md="3" lg="3" xl="3" class="mb-4 dark-grey-text">
                <h6 class="text-uppercase font-weight-bold"><strong>Useful links</strong></h6>
                <hr class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style="width: 60px" />
                <p><a href="#!" class="dark-grey-text">Your Account</a></p>
                <p><a href="#!" class="dark-grey-text">Become an Affiliate</a></p>
                <p><a href="#!" class="dark-grey-text">Shipping Rates</a></p>
                <p><a href="#!" class="dark-grey-text">Help</a></p>
                </mdb-col>
                <mdb-col md="4" lg="3" xl="3" class="mb-4 dark-grey-text">
                <h6 class="text-uppercase font-weight-bold"><strong>Contact</strong></h6>
                <hr class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style="width: 60px" />
                <p><i class="fas fa-home mr-3"></i> Sydney NSW, 2000</p>
                <p><i class="fas fa-envelope mr-3"></i> info@fvPinterest.com</p>
                <p><i class="fas fa-phone mr-3"></i> + 61 234 567 88</p>
                <p><i class="fas fa-print mr-3"></i> + 61 234 567 89</p>
                </mdb-col>
            </mdb-row>
        </mdb-container>
        <!-- Footer Section 3 -->
        <div class="footer-copyright text-center py-3 dark-grey-text">
            <mdb-container fluid>
                &copy; 2019 Copyright: <a href="/" class="dark-text"> fvPinterest.com </a>
            </mdb-container>
        </div>
    </mdb-footer>
</template>
<script>
import { mdbFooter, mdbContainer, mdbRow, mdbCol } from 'mdbvue'
export default {
    name: "Footer",
    components: {
        mdbFooter,
        mdbContainer,
        mdbRow,
        mdbCol
    }
}
</script>
<style scoped>

</style>
